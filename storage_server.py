from __future__ import print_function
import logging
import grpc
import dfs_pb2
import dfs_pb2_grpc
from DFSModule import DFS

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        # print(channel.Target)
        stub = dfs_pb2_grpc.DFSStub(channel)
        #response = stub.CreateFile(dfs_pb2.CreateFileRequest(path='mert.txt'))
        #response = stub.ListDir(dfs_pb2.ListDirRequest(path='./'))
        #response = stub.RemoveFile(dfs_pb2.RemoveFileRequest(path='mert.txt'))
        #response = stub.AppendFile(dfs_pb2.AppendFileRequest(path='mert.txt', text = "merhaba dunya"))
        #response = stub.WriteFile(dfs_pb2.WriteFileRequest(path='fatih.txt', text = "latif dunya"))
        #response = stub.TruncateFile(dfs_pb2.TruncateFileRequest(path='fatih.txt')) 
        #response = stub.ReadFile(dfs_pb2.ReadFileRequest(path='mert.txt')) 
        response = stub.SaveStorageServer(dfs_pb2.SaveStorageServerRequest(path='../',storage_server_name = 'ss1')) 
        print("Greeter client received: " + str(response.status))
        while(True):
            pass


if __name__ == '__main__':
    print("I am storage server")
    run()
