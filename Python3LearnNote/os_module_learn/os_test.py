import sys


# # print(sys.platform)
#
# s = 'h'
# si = ord(s)
# print(si)
# print(chr(104))


# def test():
#     # print('hello')
#     test()
#
#
# test()

#
# def f(*args):
#     print(*args)
#
#
# f(1,13,4,4)


# def f(a,b,c,d):
#     print(a,b,c,d)
#
# L = (1,3,4,5)
#
# f(*L)

import os



# 获取当前目录
path = os.getcwd() # /Users/yushufeng/study/Python3LearnNote/learncode
# print(path)
# print(os.path.abspath(os.path.dirname(__file__)))

# 获取上级目录
# print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

# os.path.join
# 注意：会从第一个以"/"开头的参数开始拼接，之前的参数全部丢弃

# dirname
# 去掉文件名，返回目录
# print(os.path.abspath(os.path.dirname(os.getcwd())))
p1 = "/user/jack/app/"
# print(os.path.dirname(p1))
