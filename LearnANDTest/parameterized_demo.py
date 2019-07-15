import nose_parameterized, unittest
import HtmlTestRunner

def calc(a, b):
    return a+b

case_data =[
    [10,20,30],
    [12,21,33],
    [15,21,56]
]


class MyClass(unittest.TestCase):
    @nose_parameterized.parameterized.expand(case_data)
    def test_compare(self,a,b,expect):
        actual = calc(int(a),int(b))
        self.assertEqual(actual,expect)

if __name__ == '__main__':
    unittest.main()
