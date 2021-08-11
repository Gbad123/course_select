import unittest
import sys
sys.path.append("..")

from cis4250.data import Data

class TestData(unittest.TestCase):

    def setUp(self):
        self.data = Data()

    def test_adding(self):
        self.data.add_bookmark('CIS*121')
        self.assertIn('CIS*121', self.data.bookmarks)
        self.data.add_bookmark('math*4704')
        self.data.add_bookmark('eng*1221')
        self.assertIn('CIS*121', self.data.bookmarks)
        self.assertIn('MATH*4704', self.data.bookmarks)
        self.assertIn('ENG*1221', self.data.bookmarks)

    def test_removing(self):
        self.data.remove_bookmark('math*4704')
        self.assertNotIn('MATH*4704', self.data.bookmarks)
        self.data.remove_bookmark('eng*1221')
        self.data.remove_bookmark('CIS*121')
        self.assertNotIn('CIS*121', self.data.bookmarks)
        self.assertNotIn('MATH*4704', self.data.bookmarks)
        self.assertNotIn('ENG*1221', self.data.bookmarks)

if __name__ == '__main__':
    unittest.main()