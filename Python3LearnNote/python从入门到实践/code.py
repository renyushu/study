# python 类型注解
def f(num: int) -> int:
    """
    docstring
    计算一个整数的平方
    :param num: int
    :return: int
    """
    return num ** 2

"""
集合（set）是一个无序的不重复元素序列。

创建集合方式：
    s1 = {v1, v2, v2}
    
    s2 = set(value) 创建一个空集合必须使用此方式
"""

# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)

# s3 = set('run python')
# print(s3)

# hw = "hello world".title() # 方法返回"标题化"的字符串
# print(hw)

# 如何检测字符串只含有数字：isdigit方法
# ss = '1341234134'.isdigit()
# print(ss)
# ss1 = 'dfasdf1234143'.isdigit()
# print(ss1)

# 反转字符串
# sss = 'hello python'
# print(sss[::-1])

a = "123456"
print(a[-2::])
