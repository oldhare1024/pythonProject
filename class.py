class Class1:
    x = y = 5


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Class1()
p2 = Person("py新手", 20)
p2.age = 18
# del p2.name
# del p2
print(p1.x)
print(p2.name, p2.age, sep=" ")
