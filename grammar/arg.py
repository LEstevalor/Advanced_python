"""
**kwargs 用于将关键字参数以字典（dictionary）的形式传递给函数。
*args 用于将非关键字参数以元组（tuple）的形式传递给函数。在函数定义时，可以使用 *args 来接收任意数量的位置参数
"""


def my_function(*args):
    for arg in args:
        print(arg)


my_function(1, 2, 3, 4)  # 输出：1 2 3 4


def my_function1(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")


my_function1(a=1, b=2, c=3)  # 输出：a = 1 b = 2 c = 3

# 注：pip freeze > requirements.txt  # 生成
