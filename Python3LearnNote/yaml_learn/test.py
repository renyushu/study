def func(i):
    if isinstance(i, int):
        func(i)
    else:
        print(str(i))


func(3)