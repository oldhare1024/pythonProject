import time as t


def time_master(func):
    print("程序开始运行...")
    start = t.time()
    func()
    stop = t.time()
    print("程序结束运行")
    print(f"程序运行花费时间为{(stop - start):.7f}秒")


def myfunc():
    print("I love python")


time_master(myfunc)
