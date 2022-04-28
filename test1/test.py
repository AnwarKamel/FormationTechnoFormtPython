# -*- coding: utf-8 -*-
import numpy as np

print("hI test")
name = "anfal"

print(name.lower())
print(name.upper())
print(len(name))

a = 5
b = 5.5
c = 'C'

a = 8

print(a)
print(b)
print(c)

print(" type of a = ", type(a))
print(" type of b = ", type(b))
print(" type of c = ", type(c))

# age = input("donner age : ")
# print(name," age = ", age)


num1 = input("donne num 1 = ")
num2 = input("donne num 2 = ")
num1 = float(num1)
num2 = float(num2)
some = num1 + num2
print("some = ", some)

tab1 = [1, 2, 3, 4]
tab2 = (1, 3, 10)
arra1 = np.array([1, 2, 4])
print(arra1)

for i in arra1:
    print(i)
