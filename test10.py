def print_pattern(end_letter):
    letters = [chr(i) for i in range(ord('A'), ord(end_letter)+1)]  # 创建大写字母列表
    n = len(letters)

    # 打印上半部分
    for i in range(n):
        # 打印左侧空格
        print(" " * (n - i - 1), end="")

        # 打印左侧字母
        print(letters[i] + " " * (2 * i - 1) + letters[i], end="")

        # 打印右侧字母
        print(" " * (n - i - 1))

    # 打印中间行
    print(end_letter * n + " " + end_letter * (n - 1))

    # 打印下半部分
    for i in range(n - 1, -1, -1):
        # 打印左侧空格
        print(" " * (n - i - 1), end="")

        # 打印左侧字母
        print(letters[i] + " " * (2 * i - 1) + letters[i], end="")

        # 打印右侧字母
        print(" " * (n - i - 1))


end_letter = input("请输入要作为图案结束的大写字母(A-Z)：")
print_pattern(end_letter)
