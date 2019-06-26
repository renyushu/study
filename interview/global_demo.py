

global a
a = 4


def change_a():
    global a
    a = 5


print(a)
change_a()
print(a)

dict1 = {'v1': 'k1', 'v2': 'k2'}
dict2 = {'d1': 'd2', 'd3': 'd4'}

# del dict1['v1']
print(dict1)
dict1.update(dict2)
print(dict1)