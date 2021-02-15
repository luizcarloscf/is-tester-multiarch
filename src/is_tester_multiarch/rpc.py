import time
import sys

from google.protobuf.struct_pb2 import Struct
from opencensus.ext.zipkin.trace_exporter import ZipkinExporter
from is_wire.core import Channel, StatusCode, Status, AsyncTransport
from is_wire.rpc import ServiceProvider, LogInterceptor, TracingInterceptor

from .utils import zipkin_uriparse, load_options


def increment(struct, ctx):
    if struct.fields["value"].number_value < 0:
        return Status(StatusCode.INVALID_ARGUMENT, "Number must be positive")
    time.sleep(0.2) 
    struct.fields["value"].number_value += 1.0
    return struct

def main():
    service_name = "Tester"
    filename = sys.argv[1] if len(sys.argv) == 2 else "options.json"
    options = load_options(filename=filename, print_options=True)

    channel = Channel(options.broker_uri)
    provider = ServiceProvider(channel)

    logging = LogInterceptor()
    provider.add_interceptor(logging)

    host_name, port = zipkin_uriparse(uri=options.zipkin_uri)
    exporter = ZipkinExporter(service_name=service_name,
                              host_name=host_name,
                              port=port,
                              transport=AsyncTransport)
    tracing = TracingInterceptor(exporter)
    provider.add_interceptor(tracing)

    provider.delegate(
        topic="Tester.Increment",
        function=increment,
        request_type=Struct,
        reply_type=Struct)
    provider.run() 

