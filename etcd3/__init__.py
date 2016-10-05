from __future__ import absolute_import

__author__ = 'Louis Taylor'
__email__ = 'louis@kragniz.eu'
__version__ = '0.1.0'

import grpc

from etcdrpc import rpc_pb2 as etcdrpc

channel = grpc.insecure_channel('localhost:2379')
stub = etcdrpc.KVStub(channel)

put_request = etcdrpc.PutRequest()
put_request.key = 'doot'.encode('utf-8')
put_request.value = 'toottoot'.encode('utf-8')
print(stub.Put(put_request))


class Etcd3Client(object):
    def __init__(self):
        pass

    def get(self, key):
        pass

    def put(self, key, value):
        pass
