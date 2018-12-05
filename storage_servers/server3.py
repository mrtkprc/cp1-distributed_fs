from concurrent import futures
import time
import grpc
import dfs_pb2_grpc
import dfs_pb2
import os
from DFSModule import DFS
_ONE_DAY_IN_SECONDS = 60 * 60 * 24   

def serve():
    server4 = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dfs_pb2_grpc.add_DFSServicer_to_server(DFS(), server4)
    server4.add_insecure_port('[::]:50058')
    server4.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server4.stop(0)


if __name__ == '__main__':
    print("I am storage server4")
    serve()


