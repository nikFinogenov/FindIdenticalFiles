import unittest
import argparse
import shutil
import os
import FiF
from FiF import Folder

#parser = argparse.ArgumentParser()
#args = parser.parse_args()



class MyTestCase(unittest.TestCase):
    def setUp(self):
        #self.folder = Folder()
        os.mkdir('unittestFolder')
        with open('./unittestFolder/file.txt', 'w') as f:
            f.write('Create a new text file!')

    def test_md5(self):
        self.assertEqual(FiF.md5('./unittestFolder/file.txt'), '4ba69b65a5fd2ab7a66bb4859fd89388')

    def tearDown(self):
        shutil.rmtree('./unittestFolder')

if __name__ == '__main__':
    unittest.main()
