import os
from sys import argv
import argparse

#dirpath = '/users/nikfin/Desktop/testFolder'
fileList = []
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
            fileList.append(os.path.basename(file))
    return fileList

def checkDuplicates(list):
    if len(list) == len(set(list)):
        return False
    else:
        return True

def FiF():
    file_list = list(map(lambda x: x.lower(), sorted(allFiles(dirpath))))
    #seen = set()
    dupes = []
    #dupes = [x for x in file_list if x in seen or seen.add(x)]
    for i in range(len(file_list)-1):
        if file_list[i] == file_list[i+1]:
            dupes.append(file_list[i])
    print(dupes)

if __name__ == '__main__':
    FiF()


