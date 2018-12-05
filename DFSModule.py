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

class DFS(dfs_pb2_grpc.DFSServicer):
    def CreateFile(self, request, context):
        state = False
        if(open(request.path, "w+")):
            state = True
        return dfs_pb2.CreateFileReply(status=state)
    
    def SaveStorageServer(self, request, context):
        global storage_servers_nickname
        global storage_servers_pyhsical_path
        
        storage_servers_nickname.append(request.storage_server_name)
        storage_servers_pyhsical_path.append(request.path)
        print(str(storage_servers_pyhsical_path))
        return dfs_pb2.SaveStorageServerReply(status = True, storage_server_name = request.storage_server_name, path = request.path)

    def ListDir(self, request, context):
        try:
            #files = os.listdir(request.path)
            #random_number = random.randint(0,len(storage_servers_pyhsical_path)-1)
            #print("Random number: ",random_number)
            #selected = storage_servers_pyhsical_path[random_number]
            #print("Seleceted Storages: ",selected)
            files = os.listdir(os.path.join(request.path))
            if(files):
                print("gelen list :", str(list))
                return dfs_pb2.ListDirReply(list=files,status=True)
        except:
            print("list hata ile dondu")
            return dfs_pb2.ListDirReply(list="",status=False)
   
    def RemoveFile(self, request, context):
        state = False
        if(os.remove(request.path)):
            state = True
        return dfs_pb2.CreateFileReply(status=state)

    def AppendFile(self, request, context):
        state = False

        try:
            with open(request.path, "a") as myfile:
                myfile.write(request.text)
            state = True
            return dfs_pb2.AppendFileReply(status=state)

        except:
            return dfs_pb2.AppendFileReply(status=False)
    
    def WriteFile(self, request, context):
        state = False

        try:
            with open(request.path, "w") as myfile:
                myfile.write(request.text)
            state = True
            return dfs_pb2.WriteFileReply(status=state)

        except:
            return dfs_pb2.WriteFileReply(status=False)
        
    def TruncateFile(self, request, context):
        state = False

        try:
            with open(request.path, "w") as myfile:
                myfile.write("")
            state = True
            return dfs_pb2.WriteFileReply(status=state)

        except:
            return dfs_pb2.WriteFileReply(status=False)

    def ReadFile(self, request, context):

        try:
            print("server 1 gelen path" , request.path)
            file = open(request.path,"r")
            content = file.read()
            print("content server1 :", content)
            state = True
            return dfs_pb2.ReadFileReply(fileContent=content,status=state)

        except:
            return dfs_pb2.ReadFileReply(fileContent="",status=state)       
      

     