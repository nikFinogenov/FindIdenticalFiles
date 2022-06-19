import os
from datetime import datetime

def listdir_nohidden(path):
    dirList = []
    for f in os.listdir(path):
        if not f.startswith('.'):
            dirList.append(f'{path}/{f}')
    return dirList

class File:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.creationTime = datetime.fromtimestamp(os.path.getmtime(path))
        self.nameLower = self.name.lower()

class Folder:
    fileList = []
    folderList = []
    def __init__(self, path):
        self.path = path
        for item in listdir_nohidden(path):
            if os.path.isdir(item):
                self.folderList.append(Folder(f'{path}/{os.path.basename(item)}'))
            elif os.path.isfile(item):
                self.fileList.append(File(f'{path}/{os.path.basename(item)}'))


    def sort(self):
        self.fileList.sort(key=lambda x: x.name.lower())

    def findDubl(self):
        tmp = list(map(lambda x: x.name.lower(), self.fileList))
        self.duples = []
        for i in range(len(self.fileList) - 1):
            if tmp.count(tmp[i]) > 1:
                self.duples.append(self.fileList[i])