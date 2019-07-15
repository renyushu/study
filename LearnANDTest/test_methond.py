import unittest
from common.RunMain import RunMain
from unittest.mock import MagicMock


class TestMethod(unittest.TestCase):
    def setUp(self):
        print("-------测试开始-------\n")

    def tearDown(self):
        print("-------测试结束-------\n")

    def test_case_login(self):
        data = {
            "userName": "yuuuuu2016@163.com",
            "password": "12345678",
            "sign": "c9628e50454497d5b89556b57ba523b6",
            "platform": "mobile-android"
        }

        url = "http://hkaccountcdn.chinesetvall.com/app/member/doLogin.do"
        RunMain = MagicMock(return_value=data)
        res = RunMain()
        # res = RunMain(url, 'post', data=data)
        print(res)
        # if res.res['status'] == '2':
        #     print("符合预期")
        # else:
        #     print("测试不通过")

    # @unittest.skip('test_case_login_password_error')
    def test_case_login_password_error(self):
        # print("fail")
        data = {
            "userName": "yuuuuu2016@163.com",
            "password": "123456780",
            "sign": "c9628e50454497d5b89556b57ba523b6",
            "platform": "mobile-android"
        }

        url = "http://hkaccountcdn.chinesetvall.com/app/member/doLogin.do"
        res = RunMain(url, 'post', data=data)
        # print(type(res.res))
        if res.res['status'] == '2':
            print("符合预期")
        else:
            print("测试不通过")

    def test_case_login_username_type_error(self):
        data = {
            "userName": 123455677,
            "password": "12345678",
            "sign": "c9628e50454497d5b89556b57ba523b6",
            "platform": "mobile-android"
        }
        url = "http://hkaccountcdn.chinesetvall.com/app/member/doLogin.do"
        res = RunMain(url, 'post', data=data)
        print(res.res)
        self.assertEqual(res.res['status'], '2', "符合预期")

    def test_case_login_username_lenth_error(self):
        data = {
            "userName": "yuuuuu2016999999@163.com",
            "password": "12345678",
            "sign": "c9628e50454497d5b89556b57ba523b6",
            "platform": "mobile-android"
        }
        url = "http://hkaccountcdn.chinesetvall.com/app/member/doLogin.do"
        res = RunMain(url, 'post', data=data)
        print(res.res)
        self.assertEqual(res.res['status'], '2', "符合预期")

    def test_case_login_username_none_error(self):
        data = {
            "userName": '',
            "password": "12345678",
            "sign": "c9628e50454497d5b89556b57ba523b6",
            "platform": "mobile-android"
        }

        url = "http://hkaccountcdn.chinesetvall.com/app/member/doLogin.do"
        res = RunMain(url, 'post', data=data)
        print(res.res)
        if res:
            self.assertEqual(res.res['status'], '2', "测试成功，符合预期")

    def test_case_login_username_must_error(self):
        # print("fail")
        data = {
            # "userName": "yuuuuu2016999@163.com",
            "password": "12345678",
            "sign": "c9628e50454497d5b89556b57ba523b6",
            "platform": "mobile-android"
        }

        url = "http://hkaccountcdn.chinesetvall.com/app/member/doLogin.do"
        res = RunMain(url, 'post', data=data)
        print(res.res)
        self.assertEqual(res.res['status'], '2', "测试通过，符合预期")


if __name__ == "__main__":
    unittest.main()
    # -----------------------------------------------------------
    # report_path = "../report/htmlreport.html"
    # fp = open(report_path, 'wb')
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromNames(TestMethod))
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="test report")
    # runner.run(suite)
    # suite = unittest.TestSuite()
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMethod))
    # fp = open('my_report2.html', 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp, title='My unit test',
    #     description='This demonstrates the report output by HTMLTestRunner.'
    # )
    # runner.run(suite)
    # -----------------------------------------------------------
    # example_test = TestLoader().loadTestsFromTestCase(TestMethod)
    # suite = TestSuite([example_test, ])
    # runner = HTMLTestRunner(output='report/report_1.html')
    # runner.run(suite)
