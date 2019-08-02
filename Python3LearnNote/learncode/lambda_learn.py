

def func(x, y, z):
    return x + y + z


# print(func(1, 3, 4))


f = lambda x='hello', y='python', z='ok': x + y + z
# print(f())


counters = [1, 3, 4, 89]
update = []

for x in counters:
    update.append(x+10)

# print(update)
"""
map函数会对一个序列对象中的每一个元素应用被传入的函数，并且返回一个包含了所有函数调用结果的一个列表


"""


# def inc(x):
#     return x + 10
#
#
# new = list(map(inc, counters))
# # print(new)
#
# n = list(map((lambda x: x+3), counters))
# print(n)


from functools import reduce


s = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(s)