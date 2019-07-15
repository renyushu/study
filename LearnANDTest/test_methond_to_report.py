from unittest import TestLoader, TestSuite
# from HtmlTestRunner import HTMLTestRunner
import HtmlTestRunner
from LearnANDTest.test_methond import TestMethod


example_test = TestLoader().loadTestsFromTestCase(TestMethod)
suite = TestSuite([example_test, ])
# runner = HtmlTestRunner.HTMLTestRunner().run(suite)


# h = HtmlTestRunner.HTMLTestRunner(combine_reports=True).run(suite)

# 改变报告title
runer = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name='../../reports/Myreport11', add_timestamp=False)
runer.run(suite)
