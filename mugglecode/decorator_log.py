
def log(func):
    def wrapper(*args, **kwargs):
        print('%s, %s' % (args, kwargs))
        return func(*args, **kwargs)

    return wrapper


def p(name):
    return name


def t(*args, **kwargs):
    print(args)
    print(kwargs)


p = log(p)
p('andy')
