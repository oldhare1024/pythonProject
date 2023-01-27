def debug(func):
    def wrapper():
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func()

    return wrapper


@debug
def hello(a, b, c):
    print(a, b, c)


hello("hello,", "good", "morning")
