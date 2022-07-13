import unittest
import argparse
import shutil
from FiF import *

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--silent', help='no output for human', action='store_false')
args = parser.parse_args()


class UtilitiesTestCase(unittest.TestCase):
    def setUp(self):
        os.mkdir('unittestFolder')
        with open('./unittestFolder/file.txt', 'w') as f:
            f.write('Create a new text file!')

    def test_md5(self):
        self.assertEqual(md5('./unittestFolder/file.txt'), '4ba69b65a5fd2ab7a66bb4859fd89388')

    def test_listdir_nohidden(self):
        self.assertEqual(listdir_nohidden('./unittestFolder', args), ['./unittestFolder/file.txt'])

    def tearDown(self):
        shutil.rmtree('./unittestFolder')


class FolderTestCase(unittest.TestCase):
    def setUp(self):
        os.mkdir('unittestFolder')
        os.mkdir('./unittestFolder/unittestFolderInFolder')
        with open('./unittestFolder/file.txt', 'w') as f:
            f.write('Create a new text file!')
        with open('./unittestFolder/unittestFolderInFolder/FILE.txt', 'w') as f:
            f.write('Create a copy text file!')
        self.folder = Folder('./unittestFolder', args)

    def test_find_dupl(self):
        self.folder.find_dupl(args)
        self.assertEqual(list(self.folder.res.keys()), ['file.txt'])
        self.assertEqual(list(self.folder.res.values())[0][0].name, 'file.txt')
        self.assertEqual(list(self.folder.res.values())[0][1].name, 'FILE.txt')

    def tearDown(self):
        shutil.rmtree('./unittestFolder')


if __name__ == '__main__':
    unittest.main()
