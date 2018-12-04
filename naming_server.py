from concurrent import futures
import time
import logging
import grpc
import dfs_pb2
import dfs_pb2_grpc
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DFS(dfs_pb2_grpc.DFSServicer):
    def CreateFile(self, request, context):
        print("Received Path: ", request.path)
        return dfs_pb2.CreateFileReply(message="File Created Fatihcim")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dfs_pb2_grpc.add_DFSServicer_to_server(DFS(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    print("Naming Server Started")
    serve()
    