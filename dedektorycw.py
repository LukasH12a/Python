def m(b):
    def wrapper(func):
        def in_wrapeer(*args, **kwargs):
            return func(*args, **kwargs) * b
        return in_wrapeer
    return wrapper


@m(2)
def x(a):
    return a

print(x(9))