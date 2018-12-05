from concurrent import futures
import time
import grpc
import dfs_pb2_grpc
import dfs_pb2
import os
import random

storage_servers_nickname = []
storage_servers_pyhsical_path = []

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
class FMS(dfs_pb2_grpc.DFSServicer):
    def CreateFile(self, request, context):
        print(context)
        print("file module service CreateFile")
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S1/'+ request.path
            response = stub.CreateFile(dfs_pb2.CreateFileRequest(path=p))
            #return dfs_pb2.CreateFileReply(status=response.status)
        with grpc.insecure_channel('localhost:50055') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S2/'+ request.path
            response = stub.CreateFile(dfs_pb2.CreateFileRequest(path=p))
        
        with grpc.insecure_channel('localhost:50058') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S3/'+ request.path
            response = stub.CreateFile(dfs_pb2.CreateFileRequest(path=p))
        return dfs_pb2.CreateFileReply(status=response.status)
    
    def SaveStorageServer(self, request, context):
        global storage_servers_nickname
        global storage_servers_pyhsical_path
        
        storage_servers_nickname.append(request.storage_server_name)
        storage_servers_pyhsical_path.append(request.path)
        print(str(storage_servers_pyhsical_path))
        return dfs_pb2.SaveStorageServerReply(status = True, storage_server_name = request.storage_server_name, path = request.path)

    def ListDir(self, request, context):
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S1/'+ request.path
            response = stub.ListDir(dfs_pb2.ListDirRequest(path=p))
        return dfs_pb2.ListDirReply(list = response.list, status=response.status)
        
   
    def RemoveFile(self, request, context):
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S1/'+ request.path
            response = stub.RemoveFile(dfs_pb2.RemoveFileRequest(path=p))

        with grpc.insecure_channel('localhost:50055') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S2/'+ request.path
            response = stub.RemoveFile(dfs_pb2.RemoveFileRequest(path=p))
        return dfs_pb2.RemoveFileReply(status=response.status)

        

    def AppendFile(self, request, context):
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S1/'+ request.path
            response = stub.AppendFile(dfs_pb2.AppendFileRequest(path=p, text = request.text))

        with grpc.insecure_channel('localhost:50055') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S2/'+ request.path
            response = stub.AppendFile(dfs_pb2.AppendFileRequest(path=p, text = request.text))
        return dfs_pb2.AppendFileReply(status=response.status)

    
    def WriteFile(self, request, context):
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S1/'+ request.path
            response = stub.WriteFile(dfs_pb2.WriteFileRequest(path=p, text = request.text))

        with grpc.insecure_channel('localhost:50055') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S2/'+ request.path
            response = stub.WriteFile(dfs_pb2.WriteFileRequest(path=p, text = request.text))
        return dfs_pb2.WriteFileReply(status=response.status)
        
    def TruncateFile(self, request, context):



        with grpc.insecure_channel('localhost:50052') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S1/'+ request.path
            response = stub.TruncateFile(dfs_pb2.TruncateFileRequest(path=p))

        with grpc.insecure_channel('localhost:50055') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S2/'+ request.path
            response = stub.TruncateFile(dfs_pb2.TruncateFileRequest(path=p))
        return dfs_pb2.TruncateFileReply(status=response.status)

    def ReadFile(self, request, context):
        with grpc.insecure_channel('localhost:50052') as channel:
            stub = dfs_pb2_grpc.DFSStub(channel)
            p = 'S2/'+ request.path
            print("path:", p)
            response = stub.ReadFile(dfs_pb2.ReadFileRequest(path=p))
            print("Response :", response.fileContent)
            return dfs_pb2.ReadFileReply(fileContent=response.fileContent, status = response.status)       