def Dec(func):
    def Inner(x,y):
        print("start")
        func(x,y)
    print(f"Func:{func}")
    print(f"Inner:{Inner}")
    return Inner

@Dec
def fun(a,b):
    print(a,b)
    print(a+b)
fun(10,20)
