import os
from sys import argv
import argparse
from FiF import File
from FiF import Folder

#dirpath = '/users/nikfin/Desktop/testFolder'
fileList = []
fileListOrigin = []
#dirpath = argv[1]
parser = argparse.ArgumentParser(
    prog='Find Identical Files script',
    description='You should execute script like this "python main.py /directory"',
    epilog='(c) Author NikFin'
)
#parser.add_argument('-d', '--directory', help='directory for finding')

parser.add_argument('path')
args = parser.parse_args()
dirpath = args.path



def isImageOrFolder(path, file):
    return file.lower().endswith(('.png', '.jpg', '.jpeg')) or os.path.isdir(f'{path}/{file}')

def listdir_nohidden(path):
    dirList = []
    for f in os.listdir(path):
        if not f.startswith('.') and isImageOrFolder(path, f):
            dirList.append(f'{path}/{f}')
    return dirList

def allFiles(path):
    for file in listdir_nohidden(path):
        if os.path.isdir(file):
            allFiles(file)
        elif os.path.isfile(file):
            fileList.append(f'{path}/{os.path.basename(file).lower()}')
            fileListOrigin.append(f'{path}/{os.path.basename(file)}')
    return fileList

def output(list):
    for i in list:
        print(i)

def sortPathList(elem):
    return os.path.basename(elem).lower()

def FiF():
    file_list = sorted(allFiles(dirpath), key=sortPathList)
    file_list_origin = sorted(fileListOrigin, key=sortPathList)
    tmp = list(map(lambda x: os.path.basename(x), file_list))
    duples = []
    for i in range(len(file_list) - 1):
        if tmp.count(tmp[i]) > 1:
            duples.append(file_list_origin[i])
    output(duples)




if __name__ == '__main__':
    x = Folder(dirpath)
    x.sort()
    x.findDubl()
    for i in x.duples:
        print(i.path)


