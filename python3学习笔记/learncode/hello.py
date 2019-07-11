from python3学习笔记.learncode.decorator_learn import outer
import sys


# # print(sys.platform)
#
# s = 'h'
# si = ord(s)
# print(si)
# print(chr(104))


@outer
def test():
    print('name')


test()