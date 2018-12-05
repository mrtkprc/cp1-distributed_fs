from __future__ import print_function
import logging
import grpc
import dfs_pb2
import dfs_pb2_grpc
from cryptology import encode , decode , stringToBase64 , base64ToString

def run():
    
    
        with grpc.insecure_channel('localhost:50051') as channel:
        # print(channel.Target)
            stub = dfs_pb2_grpc.DFSStub(channel)
            while(True):
                print("1: Create File\n2: Read File\n3: Write File\n4: Truncate File\n5: Remove File\n6: ListDir")
                print("Please select the number of operation you want: ",end="")
                number = input()
                number = int(number)
                if(number == 1):
                    print("Please enter the name of the file you want to create")
                    pathC = input()
                    response = stub.CreateFile(dfs_pb2.CreateFileRequest(path=pathC))
                elif(number == 2):
                    print("Please enter the name of the file you want to read")
                    pathR = input()
                    print("Please enter the key of the file for decrypting your file")
                    keyR = input()
                    response = stub.ReadFile(dfs_pb2.ReadFileRequest(path=pathR))
                    
                    fileContentR = base64ToString(response.fileContent)
                    fileContentR = decode(keyR,fileContentR)
                    print("Read File: ",fileContentR)
                elif(number == 3):
                    print("Please enter the name of the file you want to write")
                    pathW = input()
                    print("Please enter the context you want to write")
                    contextW = input()
                    print("Please enter the key of the file for encrypting your file")
                    keyW = input()
                    encrypted_msg = encode(keyW, contextW)
                    encrypted_msg = stringToBase64(encrypted_msg)
                    print(encrypted_msg)
                    response = stub.WriteFile(dfs_pb2.WriteFileRequest(path=pathW, text = encrypted_msg))
                elif(number == 4):
                    print("Please enter the name of the file you want to truncate")
                    pathT = input()
                    response = stub.TruncateFile(dfs_pb2.TruncateFileRequest(path=pathT)) 
                elif(number == 5):
                    print("Please enter the name of the file you want to remove")
                    pathRem = input()
                    response = stub.RemoveFile(dfs_pb2.RemoveFileRequest(path=pathRem))
                elif(number == 6):
                    print("Please enter the name of the file you want to list the files")
                    pathL = input()
                    response = stub.ListDir(dfs_pb2.ListDirRequest(path=pathL))
                    print(response.list)
                else:
                    print("Invalid number. Please try again")
                    return

if __name__ == '__main__':
    run()
