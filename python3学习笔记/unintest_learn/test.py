# -*- coding: utf-8 -*-
import unittest
import HTMLTestRunner
import time
import StringIO

"""
python版本：2.7
HTMLTestRunner存放路径：/Users/yushufeng/.local/share/virtualenvs/py2-hnzLho5w/lib/python2.7/ 目录下
python编译器使用的使用虚拟环境中的中的编译器，路径如下：/Users/yushufeng/.local/share/virtualenvs/py2-hnzLho5w/lib/python2.7
HTMLTestRunner文件来自：http://tungwaiyip.info/software/HTMLTestRunner_0_8_2/HTMLTestRunner.py
"""

class Test(unittest.TestCase):
    def setUp(self):
        print "start!"

    def tearDown(self):
        time.sleep(1)
        print "end!"

    def test01(self):
        print "执行测试用例01"
        self.assertEqual('a', 'b', "fail")

    def test03(self):
        print "执行测试用例03"


if __name__ == "__main__":
    # unittest.main()
    filepath = '../my.html'
    fp = StringIO(filepath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(Test('test02'))
    suite.addTest(Test('test01'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='this is first report')
    runner.run(suite)
