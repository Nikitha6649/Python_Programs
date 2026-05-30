'''def repeat(x):
    def dec(func):
        def inner():
            for i in range(x):
                func()
        return inner
    return dec
@repeat(4)
def greet():
    print("hello")
greet()'''

'''import functools
def Dec(func):
    @functools.wraps(func)
    def Inner():
        func()
    return Inner
@Dec
def fun():
    """This is Docstring"""
    print("Hello")
print(fun.__doc__)
print(fun.__name__)'''

import functools
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        print("Started: ",start)
        print(f"Sum : {func(*args, **kwargs)}")
        end = time.time()
        print(f"End : {end}")
        print("Time takem: ",end-start)
    return wrapper
@timer
def add(x,y):
    """this is a doc string"""
    su=0
    for i in range(1,x+y+1):
        su+=i
    return su
add(100000,200000)
print(add.__doc__)
print(time.asctime())
print(list(time.asctime().split()))