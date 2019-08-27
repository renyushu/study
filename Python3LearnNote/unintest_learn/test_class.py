import unittest


class TestMathFunc(unittest.TestCase):
    """Test mathfuc.py"""

    @classmethod
    def setUpClass(cls):
        print("class start\n")

    @classmethod
    def tearDownClass(cls):
        print("class over\n")

    def test_01(self):
        print('test')
        self.assertEqual(2, 2)


if __name__ == '__main__':
    print('run case')
    unittest.main(verbosity=2)
