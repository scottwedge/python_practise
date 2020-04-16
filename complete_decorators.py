def decorator_function(any_function):
    def wrapper_function(*args,**kwargs):
        '''this is wrapper function'''
        any_function(*args,**kwargs)
    return wrapper_function


@decorator_function
def add(a,b):
    '''this is add function'''
    return a + b

print(add.__doc__)
print(add.__name__)