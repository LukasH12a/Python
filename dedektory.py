def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    
    return wrapper

@uppercase
def foo():
    return 'bar'

print(foo())