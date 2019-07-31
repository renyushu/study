"""
    通用函数
"""

def tracer(func, *args, **kwargs):
    print('calling: {}'.format(func.__name__))
    return func(*args, **kwargs)


def add(a, b, c, d):
    return a+b+c+d


s = tracer(add, 1,2,34,5)
print(s)