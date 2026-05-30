#DECORATOR EX1
"""def Dec(func):
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

o/p:Func:<function fun at 0x00000238A06BF880>
Inner:<function Dec.<locals>.Inner at 0x00000238A04B3920>
start
10 20
30"""

#DECORATOR EX2
"""def Dec(func):
    def Inner(x,y):
        func(x*y,x/y)
        print("ending this function")
    return Inner
@Dec
def fun2(a,b):
    print(a,b)
    print(a+b)
fun2(10,20)

o/p:200 0.5
200.5
ending this function"""

#DECORATOR EX2
'''def  Dec(func):
    def Inner(x,y):
        if isinstance(x,str) and isinstance(y,str):
            print("Sending String")
            func(x,y)
        elif isinstance(x,(int,float)) and isinstance(y,(int,float)):
            print("Sending Integers")
            func(x,y)
        else:
            print("Sending Invalid inputs")
    return Inner
@Dec
def fun(a,b):
    print(a+b)
fun("hii","hello")

o/p:Sending String
hiihello'''

#DECORATOR EX3 using return
'''def Dec(func):
    def Inner(x,y):
        res=func(x,y)   #goes to fun2() a and b parameters
        res*=res
        return res
    return Inner
@Dec
def fun2(a,b):
    return a+b
print(fun2(15,25))   #fun2=Dec(fun2) this line runs and fun2() call goes to Inner() of Dec()

o/p:1600'''

#DECORATOR EX4
'''def Valid(func):
    def Inner():
        user=input("user:")
        password=input("password:")
        if user=="root" and password=="12345":
            res=func()
            return res
        else:
            return "Incorrect userr or password"
    return Inner
@Valid
def Secure_File():
    return "secured file"
print(Secure_File())

o/p:user:root
password:12345
secured file'''

