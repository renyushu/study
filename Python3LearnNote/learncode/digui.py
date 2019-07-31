

def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])


s = mysum([2, 3, 4, 5, 3, 4, 5])
print(s)

# lis = [1]
# print(lis[1:])

