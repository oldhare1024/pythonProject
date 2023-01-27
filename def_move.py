def outer():
    x = y = 0

    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"x现在为{x}，y现在为{y}")

    return inner


move = outer()
move(1, 2)
move(-2, 4)
