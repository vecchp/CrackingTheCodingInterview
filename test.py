"""y = 1

def f():
    def g():
        print(y)
        print(x)
        c = 3
        def p():
            print(c)
        p()
    x = 2
    g()
f()

"""
def t(a=None, b=None):
    if a == 2 or b == 2:
        return
    print(a,b)
    a = a+1 if a is not None else 0
    b = b+1 if b is not None else 0
    t(a,b)


t()