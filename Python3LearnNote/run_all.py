import unittest

start_path = '/Users/yushufeng/study/'
suite = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(start_dir=start_path, pattern='test*.py', top_level_dir=None)
print(type(discover))
suite.addTests(discover)

runner = unittest.TextTestRunner()
runner.run(suite)
