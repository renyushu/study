import unittest


class Test(unittest.TestCase):
    def test_main(self):
        for i in range(1, 10):
            if i == 2:
                self.assertEqual(i, 2)
            else:
                # print(i)
                self.assertNotEqual(i, 1)
            print(i)


if __name__ == "__main__":
    unittest.main()