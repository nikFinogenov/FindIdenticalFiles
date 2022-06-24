#!/usr/bin/env python3
import argparse
from FiF import Folder

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
if __name__ == '__main__':
    x = Folder(dirpath, args)
    x.sort()
    x.findDubl()
    if args.output:
        x.output()
    else:
        x.default_output(args)


