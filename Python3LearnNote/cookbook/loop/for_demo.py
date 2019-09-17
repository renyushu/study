# -*- coding: utf-8 -*-

"""
for使用的对象：必须是可迭代对象（iter()函数可以判断是否是可迭代对象）

数据与变量：想要方便的使用数据就要给数据起名字（否则你不知道它在哪里，叫什么，也就没有办法使用它）


"""

# print(type(1000.99))

"""

"""

mail_box = [1, 2, 3]

# def house_one():
#     mail_box = 'My precious'
#     print(mail_box)
#
#
# house_one()
# print(mail_box)
#
#
# def house_two(stuff):
#     print(stuff)
#
#
# house_two(mail_box)
# print(mail_box)


def house_three():
    # 这个函数一定会报错，想想为什么： mail_box是公共资源，只可以拿来使用不可以改变此数据
    # mail_box
    print(mail_box)


# house_three()
#
# str = 'My preciousfdgd hello'
# p1 = str.split()
# print(p1)

# # 分割字符串
# string = "哈利、罗恩、赫敏"
# string_list = string.split('、')
# print(string_list)

# 分割字符串
string = "哈利、罗恩、赫敏"
list = string.split("、")
print(list)
# print(string)