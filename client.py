from __future__ import print_function
import logging
import grpc
import dfs_pb2
import dfs_pb2_grpc
from cryptology import encode , decode , stringToBase64

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        # print(channel.Target)
        stub = dfs_pb2_grpc.DFSStub(channel)
        #response = stub.CreateFile(dfs_pb2.CreateFileRequest(path='mert.txt'))
        #response = stub.RemoveFile(dfs_pb2.RemoveFileRequest(path='mert.txt'))
        #response = stub.TruncateFile(dfs_pb2.TruncateFileRequest(path='mert.txt')) 
        
        #response = stub.AppendFile(dfs_pb2.AppendFileRequest(path='mert.txt', text = "merhaba dunya"))
        response = stub.ReadFile(dfs_pb2.ReadFileRequest(path='mert.txt')) 
        response = stub.ListDir(dfs_pb2.ListDirRequest(path=''))
        encrypted_msg = encode("key", "merhaba dunyamerhaba dunyamerhaba dunyamerhaba dunya")


        
        encrypted_msg = stringToBase64(encrypted_msg)
        print(encrypted_msg)
        response = stub.WriteFile(dfs_pb2.WriteFileRequest(path='ff.txt', text = encrypted_msg))
        
        

        #print("Client.py file Content: " + str(response.fileContent))
        #print(type((response.fileContent)))
if __name__ == '__main__':
    run()
