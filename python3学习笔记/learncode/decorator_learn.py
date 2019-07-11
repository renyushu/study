
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


# def outer(func): # 装饰器是一个带有函数作为参数并返回一个新函数的必包
#     def inner():
#         print("日志记录开始")
#         func()  # 业务函数
#         print("记录日志结束")
#     return inner
#
#
# # foo = outer(foo)
# # foo()
#
# @outer # python语法糖，用在函数定义处，调用函数之前会先调用装饰器
# def print_h():
#     print('hello world')


# p = outer(print_h)
# p()


# print_h()



# 写一个带参数的装饰器
# 那些地方适合使用装饰器呢？ 但凡是在多个地方出现雷同的代码块，且这些代码与核心业务没有关联的都可以用装饰器来解决，装饰器不仅能减少代码量，还使代码逻辑更清晰，可读性更强
# 业务函数

# def my_upper(text):
#     value = text.upper()
#     return value


# print(my_upper('hello'))

# 需求1：需要对转换的字符串包裹一层html标签 <p>HELLO</p>
# 需求2：在1的基础上在包裹一层div标签
# ....

# 你总不能一个一个去该函数吧，如果这样的需求一个接一个，这样的函数有n个。。。答案就是：使用装饰器


# def tag(func):
#     def wrapper(text):
#         value = func(text)
#         return '<p>' + value + '</p>'
#     return wrapper

#
# def tag(h,name):
#     print(locals())
#     print(globals())
#     def decorator(func):
#         def wrapper(text): # 这个参数从哪里来
#             print(locals())
#             value = func(text)
#             return "<{h}><{name}>{value}<{name}><{h}>".format(h=h,name=name, value=value)
#         return wrapper
#
#     return decorator
#
#
# @tag('h', 'div')     # @tag: my_upper = tag(my_upper)
# def my_upper(text):
#     value = text.upper()
#     return value
#
#
# print(my_upper('hello'))

# # 给函数实现一个日志功能，日志里面记录函数名，函数执行所花的时间，通过指定参数控制日志级别
# #
#
#
# def a(name):
#     return name
#
#
# def wrapper(level):
#     def log_info(func):
#         pass
#
#     return log_info


# ----------------------------------------

# 12步教你理解python装饰器
# 1，函数
# 2，作用域： 每个函数都会创建一个作用域，函数拥有自己的命名空间，这意味着当在函数体里遇到变量时，python首先在该函数的命名空间中查找
#       local 和 global


# a_string = 'this is a global variable'
# def foo():
#     print(locals()) #
#
#
# foo() # 将函数内部的local namespace里的内容打印出来
# print(globals()) # globals()返回的是一个字典对象，它所包含了所有python知道的变量名

# 3，变量解析规则
# **python的作用域规则：变量的创建总会创建一个新的local变量，但是变量的访问（包括修改）会先查找local作用域然后顺着最邻近的作用域去寻找匹配**
# **全局变量可以被访问到（如何是可变类型，甚至是可以被改变），但是（默认情况下）不能被赋值**

# 变量的生命周期
# def foo():
#     x =1 # 每当函数被调用时，变量X被创建，调用结束时变量被销毁。每次调用namespace都会重新构建
#     print(x)
#
# print(x)

# 5，函数的参数
#