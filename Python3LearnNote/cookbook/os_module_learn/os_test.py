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



# # 获取当前目录
# path = os.getcwd() # /Users/yushufeng/study/Python3LearnNote/learncode
# # print(path)
# # print(os.path.abspath(os.path.dirname(__file__)))
#
# # 获取上级目录
# # print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
# print(os.path.abspath(os.path.join(os.getcwd(), "..")))
#
# # os.path.join
# # 注意：会从第一个以"/"开头的参数开始拼接，之前的参数全部丢弃
#
# # dirname
# # 去掉文件名，返回目录
# # print(os.path.abspath(os.path.dirname(os.getcwd())))
# p1 = "/user/jack/app/"
# # print(os.path.dirname(p1))
import os


def print_directory_contents(s_path):
    """
    这个函数接收文件夹的名称作为输入参数
    返回该文件夹中文件的路径
    以及其包含文件夹中文件的路径
    """
    for s_child in os.listdir(s_path):
        s_child_path = os.path.join(s_path, s_child)
        if os.path.isdir(s_child_path):
            print_directory_contents(s_child_path)
        else:
            print(s_child_path)


print_directory_contents('/Users/yushufeng/study/ui_auto_learn')
# print(os.listdir('../..'))