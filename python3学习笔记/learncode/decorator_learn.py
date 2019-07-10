
#
# def foo(num):
#     return num + 1
#
#
# func = foo
# print(func(2))


# # 函数嵌套
#
# def outer():
#     x = 1
#
#     def inner():
#         print(x)
#     inner()
#
# outer()


# # 闭包
#
# def outer(x):
#     def inner():
#         print(x)
#
#     return inner
#
#
# closure = outer(1)
# closure()


# 装饰器

def foo():
    print("foo")


# ## 需求一：需要在函数执行的时候加上日志
#
#
# def foo():
#     print("记录日志开始")
#     print("foo")
#     print("记录日志结束")
#     # 缺点是：需要改变原有的代码结构，把日志逻辑加载上去，如果还有好几十个这样的函数需要加日志功能，也必须这样做？
#     # 那么有没有不改变日志的前提下实现日志功能呢？
#     # 答案就是使用： 装饰器


def outer(func): # 装饰器是一个带有函数作为参数并返回一个新函数的必包
    def inner():
        print("日志记录开始")
        func()  # 业务函数
        print("记录日志结束")
    return inner


# foo = outer(foo)
# foo()

@outer # python语法糖，用在函数定义处，调用函数之前会先调用装饰器
def print_h():
    print('hello world')


# p = outer(print_h)
# p()


print_h()

















