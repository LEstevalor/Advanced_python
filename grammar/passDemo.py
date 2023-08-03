"""
pass 语句在 Python 中是一个空操作（no-operation）语句，它的作用是在代码块中起到占位符的作用
"""


def my_function():
    pass


class MyClass:
    pass


for i in range(10):
    if i % 2 == 0:
        pass  # 对于偶数，不执行任何操作
    else:
        print(i)  # 对于奇数，打印数字
