import os
class File:
    fileList = []
    fileListOrigin = []
    def __init__(self, dirpath):
        self.dirpath = dirpath


    def isImageOrFolder(self, path, file):
        return file.lower().endswith(('.png', '.jpg', '.jpeg')) or os.path.isdir(f'{path}/{file}')

    def listdir_nohidden(self, path):
        dirList = []
        for f in os.listdir(path):
            if not f.startswith('.') and self.isImageOrFolder(path, f):
                dirList.append(f'{path}/{f}')
        return dirList

    def allFiles(self, path):
        for file in self.listdir_nohidden(path):
            if os.path.isdir(file):
                self.allFiles(file)
            elif os.path.isfile(file):
                self.fileList.append(f'{path}/{os.path.basename(file).lower()}')
                self.fileListOrigin.append(f'{path}/{os.path.basename(file)}')
        return self.fileList

    def output(self, list):
        for i in list:
            print(i)

    def sortPathList(self, elem):
        return os.path.basename(elem)

    def mainFunc(self):
        file_list = sorted(self.allFiles(self.dirpath), key=self.sortPathList)
        file_list_origin = sorted(self.fileListOrigin, key=self.sortPathList)
        tmp = list(map(lambda x: os.path.basename(x), file_list))
        duples = []
        for i in range(len(file_list) - 1):
            if tmp.count(tmp[i]) > 1:
                duples.append(file_list_origin[i])
        self.output(duples)