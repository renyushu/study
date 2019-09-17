
def multiply(*args):
    z = 1
    for num in args:
        z = z * num
    print(z)

# multiply(2)
# multiply(2, 3)
# multiply(2, 3, 3, 4, 4, 5)


def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(kwargs_1='hello', kwargs_2='world', kwargs_3='python') # {'kwargs_1': 'hello', 'kwargs_2': 'world', 'kwargs_3': 'python'}
