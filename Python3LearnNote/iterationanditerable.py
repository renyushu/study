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

# 生成器机制：一边循环一边计算
#
# L = [x * x for x in range(10)]
# print(L)
#
# L2 = (x * x for x in range(10))
#
# for i in L2: # 生成器是可迭代对象
#     print(i)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# print(fib(3)) # 生成器执行机制：每次调用next()的时候执行，遇到yield返回
            # 调用generator时：首先要生成一个generator对象，然后用next()函数不断获得下一个返回值
            # 一般不使用next()来迭代，而是使用for循环来迭代


# for i in fib(5):
    # print(i)

g = fib(6)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break