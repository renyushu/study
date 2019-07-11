# 12步教你理解python装饰器
# 1，函数
# 2，作用域： 每个函数都会创建一个作用域，函数拥有自己的命名空间，这意味着当在函数体里遇到变量时，python首先在该函数的命名空间中查找
#       local 和 global

a_string = 'this si a global variable'
def foo():
    print(locals())

foo()
print(globals())