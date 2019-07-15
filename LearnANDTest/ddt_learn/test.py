import unittest
import paramunittest

cases = [
            ['user1', 'password1', 'true'],
            ['user2', 'password1', 'true'],
            ['user3', 'password1', 'true']
        ]


@paramunittest.parametrized(*cases)
class TestDemo(unittest.TestCase):
    def setParameters(self, user, password, result):    # 与字典的key一一对应
        self.user = user
        self.password = password
        self.result = result

    def testCase(self):
        print(f'user: {self.user}')
        print(f'password: {self.password}')
        print(f'result: {self.result}')
        self.assertEqual('true', self.result)


if __name__ == '__main__':
    unittest.main()
