# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunner
from io import StringIO


class Test(unittest.TestCase):

    def add(self):
        return 1 + 1

    # def divide(self):
    #     return 0 / 0

    def test_1(self):
        '''test_1 func'''
        print('test_1')
        self.assertEqual(2, self.add())

    # def test_2(self):
    #     '''test_2 func'''
    #     print('test_2')
    #     self.assertEqual(3, self.add())

    def test_3(self):
        '''test_3 func'''
        self.assertEqual(3, self.add())


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test))
    # fp = StringIO('my_report.html', 'wb')
    # print('stringio')
    # print(fp.getvalue())
    fp = open('my_report.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp, title='My unit test',
        description='This demonstrates the report output by HTMLTestRunner.'
    )
    runner.run(suite)
