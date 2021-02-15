from is_wire.core import Channel, Message, Subscription
from google.protobuf.struct_pb2 import Struct
import socket

channel = Channel("amqp://guest:guest@10.10.2.7:30000")
subscription = Subscription(channel)

# Prepare request
struct = Struct()
struct.fields["value"].number_value = 1.0
request = Message(content=struct, reply_to=subscription)
# Make request
channel.publish(request, topic="Tester.Increment")

# Wait for reply with 1.0 seconds timeout
try:
    reply = channel.consume(timeout=1.0)
    struct = reply.unpack(Struct)
    print('RPC Status:', reply.status, '\nReply:', struct)
except socket.timeout:
    print('No reply :(')