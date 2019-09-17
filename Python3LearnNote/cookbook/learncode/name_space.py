# 12步教你理解python装饰器
# 1，函数
# 2，作用域： 每个函数都会创建一个作用域，函数拥有自己的命名空间，这意味着当在函数体里遇到变量时，python首先在该函数的命名空间中查找
#       local 和 global

# a_string = 'this si a global variable'
# def foo():
#     print(locals())
#
# foo()
# print(globals())


# X = 99
# #
# #
# # def f1():
# #     # X = 88
# #
# #     def f2():
# #         print(X)
# #     f2()
# #
# # f1()
# #
# #
# # def f1():
# #     # X = 88
# #
# #     def f2():
# #         print(X)
# #     return f2


# def f1():
#     x = 88
#     f2(x)
#
#
# def f2(x):
#     print(x)
#
#
# f1()


def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(state, label)
        state += 1
    return nested


f = tester(9)
f('hello')

f('world')
f('python')