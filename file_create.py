import os
def FileListDir(path):
    try:
        files = os.listdir(path)
        if(files):
            for name in files:
                print(name)
            return 0
    except:
        return -1        

    


def FileCreate(path):
    if(open(path, "w+")):
        return 0
    return -1


def FileAppend(path, text):
    with open(path, "a") as myfile:
        myfile.write(text)

def FileWrite(path, text):
    with open(path, "w") as myfile:
        myfile.write(text)

def FileTruncate(path):
    FileWrite(path, "")

def FileRemove(path):
    if(os.remove(path)):
        return 0
    return -1


def FileRead(path):
    file = open(path, "r")
    print (file.read())

# def FileDownlod(path):
#     file = open(path, "r")
#     fileContent = file.read()

if __name__ == "__main__":
    FileTruncate("la.txt")
