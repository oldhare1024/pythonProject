a = 100
b = 200


def fun1():
    a = 150
    return a


def fun2():
    global b
    b = 250
    return b


print(fun1(), a)
print(fun2(), b)
