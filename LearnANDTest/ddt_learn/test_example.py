from ddt import data, unpack, ddt
import unittest


@ddt
class TestExample(unittest.TestCase):
    def setUp(self):
        pass

    @data([1, 2, 3, 3, 4, 3])
    @unpack
    def test_add(self, *args):
        two = args[1]
        print(two)


if __name__ == "__main__":
    unittest.main(verbosity=2)
