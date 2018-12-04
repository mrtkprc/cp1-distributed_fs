from __future__ import print_function
import logging

import grpc

import dfs_pb2
import dfs_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = dfs_pb2_grpc.DFSStub(channel)
        response = stub.CreateFile(dfs_pb2.CreateFileRequest(path='latif.txt'))

    print("Greeter client received: " + response.message)

if __name__ == '__main__':
    run()
