"""
鸭子模型
一种多态模型
"""


class Duck:
    def quack(self):
        return "Quack!"


class Dog:
    def quack(self):
        return "Woof!"


def make_sound(animal):
    print(animal.quack())


duck = Duck()
dog = Dog()

make_sound(duck)  # 输出 "Quack!"
make_sound(dog)  # 输出 "Woof!"
