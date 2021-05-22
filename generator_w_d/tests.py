from main_for_tests import bp
import unittest

class NameTestCase(unittest.TestCase):
    def test_num1_bigger_then_num2(self):
        name = 'Merge Intervals'
        link = 'https://leetcode.com/problems/merge-intervals/'
        code = "class Solution:\n       def merge(self, intervals: List[List[int]]) -> List[List[int]]:\n              # your solution\n              return [[]]"
        file = 'test1.md'
        open(file, 'w').close
        bp(name, link, code, file)
        self.assertEqual(open(file,'r').readlines(), open('test1_check.md','r').readlines())
    def test_num1_bigger_then_num3(self):
        name = 'Merge Intervals'
        link = 'https://leetcode.com/problems/merge-intervals/'
        code = "class Solution:\n       def merge(self, intervals: List[List[int]]) -> List[List[int]]:\n              # your solution\n              return [[]]"
        file = 'test1.md'
        open(file,'w').close
        bp(name, link, code, file)
        name = 'Insert Interval'
        link = 'https://leetcode.com/problems/insert-interval/'
        code = "class Solution:\n    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:\n           # your solution\n           return [[]]"
        file = 'test1.md'
        bp(name, link, code, file)
        self.assertEqual(open(file,'r').readlines(), open('test1_check2.md','r').readlines())



if __name__ == "__name__":
    unittest.main()