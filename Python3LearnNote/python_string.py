#
# # p = r"xxx.ng"
# # str = r"hhhh"
# # print(str)
# # print(p)
#
# """
# 原始字符串：带有前缀 r' ' or R' '  ,在原始字符串字面值中，'\ U' 和 ' \ u' 转义形式不会被特殊对待
#
# """
#
# # string = 'hello'
# # s = r'{}'.format(string)
# # print(s)
# # ss = 'r' + "'hhh'"
# # print(ss)
#
#
# s = '8TFDU18802000479\tdevice\n'
# print(s)
# # print(s.replace('\n', ''))
# print('h')

import copy


a = [1, 3, 4]
b = copy.copy(a)
# b = copy.copy(l)
# c = copy.deepcopy(a)
# print(id(a), id(b), id(c))
# print(a, b, c)
#
# a.append(5)
# print(id(a), id(b), id(c))
# print(a, b, c)
print(a is b)

"""
浅拷贝：对象的元素指向之前的内存地址
"""
print(a[0] is b[0])

