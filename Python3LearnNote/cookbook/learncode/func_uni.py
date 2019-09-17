"""
    通用函数
"""

# def tracer(func, *args, **kwargs):
#     print('calling: {}'.format(func.__name__))
#     return func(*args, **kwargs)
#
#
# def add(a, b, c, d):
#     return a+b+c+d
#
#
# s = tracer(add, 1,2,34,5)
# print(s)

import os

p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
case_path = os.path.join(p, 'case/login.yaml')
# p1 = p.split('/')
print(case_path)
print(__file__)