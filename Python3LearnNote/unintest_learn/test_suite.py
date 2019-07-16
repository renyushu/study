from Python3LearnNote.unintest_learn.test_mathfunc import *
from Python3LearnNote.unintest_learn.test import *
import unittest


if __name__ == '__main__':
    suite = unittest.TestSuite()

    # case name
    # tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    # suite.addTests(tests)

    # 使用addTests + TestLoader传入模块
    # suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc')) # 传入单个模块

    suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc', 'test'])) # 添加多个模块（文件）
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)

    # 将结果输入到文件,报告在同目录下
    with open('report.txt', 'a') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)