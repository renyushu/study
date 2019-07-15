
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


# def wrapper(level):
#     print(globals())
#     print('globals run')
#     # print(locals())
#     def log_info(func):
#         # print(locals())
#         print(level)
#         print(func.__name__)
#         print('time')
#
#         def inner(text):
#             # print(locals())
#             return func(text)
#         return inner
#     return log_info
#
#
# # @wrapper('info')
# def a(name):
#     return name
#
#
# wra = wrapper('info', a('andy'))

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

# 5，函数的参数：参数名成为了该函数的local变量
# # 6，内嵌函数
# #   python允许创建嵌套函数，这意味这我们可以在函数内声明函数并且所有的作用域和声明周期规则也同样适用
#
# y = 2
# def outer():
#     x = 1
#     def inner():
#         print(x) # python寻找一个名为x的local变量，但是失败了，然后在最邻近的外层作用域里搜寻，这个作用域是另外一个函数（inner函数对外层作用域拥有访问权限，最起码有读和修改的权限）
#
#         print(y)
#     return inner
#
# inner = outer()
# inner()

# 7，函数是一等公民
# 函数可以作为参数传入函数中，也可以当作返回值

# def add(x, y):
#     return x + y
#
# def apply(func, x, y):
#     return func(x, y)
#
# res  = apply(add, 2, 3)
# print(res)

# def outer():
#     def inner():
#         print('inside inner')
#     return inner

"""
每当outer函数被调用时inner函数就会重新被定义一次，但是如果inner函数不被（outer)返回那么当超出outer的作用域后，inner将不复存在了
"""

# 8，闭包
#
# def outer():
#     x = 1
#     def inner():
#         print(x)
#     return inner
#
# foo = outer()
#             # 按照python的作用域规则，这是没有问题的
#              # 但是从python变量的生命周期来看，变量x是outer的local变量，这意味着只有当outer函数运行时它才存在。只有当outer返回后我们才能调用inner，因此依照
#              # 这点来看，我们调用 inner的时候，x已经不复存在了，那么某个运行时错误可能会出现。
#              # 事实上并非如此，返回的函数inner正常运行。
#              #  python支持一种叫做闭包的特性，这意味着定义于非全局作用域的inner函数在定义时记得它们的外层作用域长什么样。
#             #  这可以通过查看inner函数的func_closure属性来查看，它包含了外层作用域里的变量。
# print(foo.func_closure)

# 9, 装饰器: 一个decorator只是一个带有一个函数作为参数并返回一个替换函数的闭包

# def outer(func):
#     def inner():
#         print('before some func')
#         ret = func()
#         return ret + 1
#     return inner
#
#
# def foo():
#     return 1
#
# inner = outer(foo)
# i = inner()
# print(i)

# 10,语法糖

# 11，*args and **kwargs
# def one(*args):
#     print(*args)
#
# # print(one())
# # print(one(1,2))
# one()
# one(1, 3)


# def multiply(*args):
#     z = 1
#     for num in args:
#         z = z * num
#     print(z)
#
# # multiply(2)
# # multiply(2, 3)
# # multiply(2, 3, 3, 4, 4, 5)
#
#
# def print_kwargs(**kwargs):
#     print(kwargs)
#
#
# print_kwargs(kwargs_1='hello', kwargs_2='world', kwargs_3='python') # {'kwargs_1': 'hello', 'kwargs_2': 'world', 'kwargs_3': 'python'}

# def print_values(**kwargs):
#     for key, value in kwargs.items():
#         print('The value of {} is {}'.format(key, value))
#
#
# print_values(my_name='Sammy', your_name='Casey', her_name='Pig')
# # 使用**kwargs为我们提供了在程序中使用关键字参数的灵活性。当我们使用**kwargs作为参数时，我们不需要知道我们最终想要传递给函数的参数数量


# # 12,更通用的装饰器
# def logger(func):
#     def inner(*args, **kwargs):
#         print('Arguments were %s, %s' % (args, kwargs))
#         return func(*args, **kwargs)
#
#     return inner
#
#
# @logger
# def foo1(x, y=2):
#     return x * y
#
# foo1(5, 4)
# foo1(3)
# # foo1()
#
#
# @logger
# def foo():
#     return 2


import functools
from functools import wraps


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)
        return wrapper
    return decorator


# @log('run')
def now(name):
    print(name)


# now = log('run')(now('python')) 这是错误调用方式
now = log('run')(now)
now('n')

"""
log返回的是一个函数，返回的哪个函数也是返回一个函数
"""
# def fu(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# fu('222', 1, 3, kw_1='python')