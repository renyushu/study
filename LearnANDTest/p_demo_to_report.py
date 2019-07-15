from LearnandTesting.parameterized_demo import Login
import unittest
import HtmlTestRunner


if __name__== '__main__':
    suite = unittest.TestSuite()#定义个空的测试集合
    suite.addTests(unittest.TestLoader().loadTestsFromNames(Login))
    runner = HtmlTestRunner.HTMLTestRunner()
    runner.run(suite)
