from concurrent import futures
import time
import grpc
import dfs_pb2_grpc
import dfs_pb2
import os
_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class DFS(dfs_pb2_grpc.DFSServicer):
    def CreateFile(self, request, context):
        state = False
        if(open(request.path, "w+")):
            state = True
        return dfs_pb2.CreateFileReply(status=state)

    def ListDir(self, request, context):
        try:
            files = os.listdir(request.path)
            if(files):
                return dfs_pb2.ListDirReply(list=files,status=True)
        except:
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
        state = False

        try:
            file = open(request.path,"r")
            content = file.read()
            state = True
            return dfs_pb2.ReadFileReply(fileContent=content,status=state)

        except:
            return dfs_pb2.ReadFileReply(fileContent="",status=state)       
      

     