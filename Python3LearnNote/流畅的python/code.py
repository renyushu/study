#
# a = zip((1, 3, 4, 32))
# print(list(a))
#

# l = [value ** 2 for value in range(1, 11)]
# # print(l)
# #
# # L = [i for i in range(1, 1000001)]
# # min_sum = min(L)
# # max_sum = max(L)
# # print(min_sum, max_sum)
# #
# # import time
# #
# # t0 = time.time()
# # sum_L = sum(L)
# # t = time.time() - t0
# # print(t, sum_L)

# L = [x for x in range(3, 31) if x % 3 == 0]
# for s in L:
#     print(s)

# L = [x ** 3 for x in range(1, 11)]
# for s in L:
#     print(s)

d = {'k1': 'v1', 'k2': 'v2', 'k23': 'jj', 'k3': 'v3'}


# for k in d.keys():
#     print(k)

# # 按顺序遍历字典中的所有键
# for k in sorted(d.keys()): # sorted方法：可对所有可迭代的对象进行排序操作， 默认升序排列
#     print(k)


def f():
    print('1')
    b = yield
    print(b)

if __name__ == '__main__':
    g = f()
    print(type(f()))
    print(iter(g) is g)
    for g in g:
        print(g)
