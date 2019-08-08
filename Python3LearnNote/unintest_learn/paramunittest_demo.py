import unittest
import paramunittest


@paramunittest.parametrized(
    {'a': 5, 'b': {'c': {'cc': 'ccvalue'}}, 'd': 'v4', 'e': 'v5'},
    {'a': 5, 'b': {'c': {'cc': 'ccvalue'}}, 'd': 'v4', 'e': 'v5'}
)
class TestBar(unittest.TestCase):
    def setParameters(self, a, b, d, e):
        self.a = a
        self.b = b['c']
        self.d = d
        self.e = e

    def testLess(self):
        # self.assertLess(self.a, self.b)
        print('a: ' + str(self.a))
        print('b: ' + str(self.b))
        print('d: ' + str(self.d))
        print('e: ' + str(self.e))


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""
    paramunittest参数化测试框架说明
    
        *list
            a = list[0]
            b = list[1]
                ...
                
        *dic {'k1': 'v1', 'k2': 'v2'}
            a = 'v1'
            b = 'v2'
test_login_login:
  case_name: 
  case_module: login
  case_id: 1
  request_method: post
  host: http://hkaccountcdn.chinesetvall.com/app/member/doLogin.do
  data:
    userName: yuuuuu2016@163.com
    password: 12345678
    sign: c9628e50454497d5b89556b57ba523b6
    platform: mobile-android
  hearder:
  token:
  except_result:
    status: 1
  actual_result:
    photo:
    status: 1
    token: 605db0f924896ef710513397cfcfc9f5
    userName: yuuuuu2016@163.com



"""