from unittest import TestLoader, TestSuite
from HtmlTestRunner import HTMLTestRunner
from LearnANDTest.unit_test import TestStringMethods


example_test = TestLoader().loadTestsFromTestCase(TestStringMethods)
suite = TestSuite([example_test, ])
runner = HTMLTestRunner(output='../report/')

runner.run(suite)
