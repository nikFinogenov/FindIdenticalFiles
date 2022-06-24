import os
from datetime import datetime
import argparse
from texttable import Texttable
import hashlib

parser = argparse.ArgumentParser(
    prog='Find Identical Files script',
    description='You should execute script like this "python FiF.py /directory"',
    epilog='(c) Author NikFin'
)

parser.add_argument('-s', '--hidden', help='include hidden files', action='store_true')
parser.add_argument('-o', '--output', help='show table on exit', action='store_true')
parser.add_argument('-d', '--delimiter', help='update delimiter for default output', type=str, default='\t')
parser.add_argument('path')

args = parser.parse_args()
dirpath = args.path



def listdir_nohidden(path):
    dirList = []
    for f in os.listdir(path):
        if not f.startswith('.') or args.hidden:
            dirList.append(f'{path}/{f}')
    return dirList

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

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
        self.fileList.sort(key=lambda x: x.nameLower)

    def findDubl(self):
        tmp = list(map(lambda x: x.nameLower, self.fileList))
        self.duples = []
        for i in range(len(self.fileList) - 1):
            if tmp.count(tmp[i]) > 1:
                self.duples.append(self.fileList[i])

    def default_output(self):
        for i in self.duples:
            print(i.name,args.delimiter,i.path,args.delimiter,md5(i.path),args.delimiter,i.creationTime)

    def output(self):
        t = Texttable()
        t.set_cols_width([15, 50, 40, 20])
        t.add_row(["File name", "Path", "Md5", "Creation Time"])
        for i in self.duples:
            t.add_row([i.name, i.path, md5(i.path), i.creationTime])
        print(t.draw())
if __name__ == '__main__':
    x = Folder(dirpath)
    x.sort()
    x.findDubl()
    if args.output:
        x.output()
    else:
        x.default_output()