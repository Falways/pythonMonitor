#!/usr/bin/python3

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class Person:
    def sayName(self,username):
        return username;
b = Person()
x = Complex(3.0, -4.5)
print(x.r, x.i)  # 输出结果：3.0 -4.5
print(b.sayName('xuhang'))