def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    
    return wrapper

def repeat(times):
    def wrapper(func):
        def inner_wrapper(*args, **kwargs):
            response = []
            for _ in range(times):
                response.append(func(*args, **kwargs))
                
            return response
        return inner_wrapper
    return wrapper

@repeat(3)
def hello(name):
    return f'Hello {name}'

a = hello('Karusiu')

print(hello('Karusia'))