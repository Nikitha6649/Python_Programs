def calc():
    a = int(input())
    b = int(input())
    c = input("+,-,*,/,% : ")
    def add():
        return a+b
    def sub():
        return a-b
    def mul():
        return a*b
    def div():
        return a/b
    def mod():
        return a%b

    if c=="+":
        print(add())
    elif c=="-":
        print(sub())
    elif c=="*":
        print(mul())
    elif c=="/":
        print(div())
    else:
        print(mod())
calc()