from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from LearnANDTest.test_methond_v1 import Test


example_tests = TestLoader().loadTestsFromTestCase(Test)
suite = TestSuite([example_tests, ])
runner = HTMLTestRunner()
runner.run(suite)
