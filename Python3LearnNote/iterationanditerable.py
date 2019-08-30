# iteration
# a_list = [1, 2, 3]
# for i in a_list:
#     print(i)

# python可迭代类型: list tuple string dict set file
# 如果提供了 __iter__() __getitem__()方法, 那么该对象也是可迭代的

# 迭代器抽象的是一个数据流，是只允许迭代一次的对象。
# 迭代器的__iter__()方法返回迭代器自身，因此也是可迭代的

# 迭代器协议： 至的是容器类需要包含一个特殊方法


# def func():
#     for x in range(1,3):
#         print(x ** 2)
#
# sum = func()

# def square():
#     for x in range(4):
#         yield x ** 2
# square_gen = square()
# for x in square_gen:
#     print(x)

#
# def f1():
#     yield 1
#     yield 2
#     yield 3
#
# for item in f1():
#     print(item)

