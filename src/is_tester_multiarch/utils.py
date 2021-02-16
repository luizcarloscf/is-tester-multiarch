import re

from is_wire.core import Logger
from google.protobuf.json_format import Parse

from .conf.options_pb2 import TesterOptions


def zipkin_uriparse(uri: str = "http://localhost:9411"):
    """
    Parse Zipkin uri using RegEx (regular expression). Raises a critical error if uri does't match
    format expected.

    Parameters
    ----------
    uri: str
        Zipkin uri.

    Returns
    -------
    tuple
        A tuple contaning hostname and port.

    Example
    -------
        >>> from utils import zipkin_uriparse
        >>> uri = "http://zipkin.default:9411"
        >>> zipkin_uriparse(uri=uri)
        ('zipkin.default', '9411')

    """
    log = Logger(name="ZipkinUriParse")
    zipkin_ok = re.match("http:\\/\\/([a-zA-Z0-9\\.]+)(:(\\d+))?", uri)
    if not zipkin_ok:
        log.critical("Invalid zipkin uri \"{}\", expected http://<hostname>:<port>", uri)
    host_name, port = zipkin_ok.group(1), zipkin_ok.group(3)

    return host_name, port


def load_options(filename: str = 'options.json', print_options: bool = True):
    """
    Load a json file and parse into protobuf object. Raises critical error if cannot open or read.
    file.

    Parameters
    ----------
    filename: str
        name of json file.
    print_options: bool
        if true, print file loaded.

    Returns
    -------

    options_pb2.TesterOptions
        Protobuf object that defines options passed as argument.
    """
    log = Logger(name='LoadingOptions')
    try:
        with open(filename, 'r') as f:
            try:
                op = Parse(f.read(), TesterOptions())
                if print_options:
                    log.info('TesterOptions: \n{}', op)
                return op
            except Exception as ex:
                log.critical('Unable to load options from \'{}\'. \n{}', filename, ex)
    except Exception as ex:
        log.critical('Unable to open file \'{}\'. \n{}', filename, ex)
