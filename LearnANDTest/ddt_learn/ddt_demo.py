from ddt import ddt, data, unpack
import unittest


@ddt
class TestOdd(unittest.TestCase):

    @data(3, 4, 12, 23)
    def runTest(self, value):
        self.assertEqual(3, value)


