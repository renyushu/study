L = [1,2,3]

# print(dir(L))
#
# for a in dir(L):
#     print(a)
#
# print(help(L))

L2 = [1, 2, 3, 4, 5, 34]


def intersect(seq1, seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res


# res = intersect(L, L2)
# print(res)
#
# L3 = [x for x in L if x in L2]

intersect.count = 1
# print(dir(intersect))

import time
import paramunittest


import sys


print(sys.modules.keys())