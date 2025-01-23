#ex1
import math

def convertion(degrees):
    return degrees * (math.pi/180)

degrees = float(input("Input degree: "))

print("Output radian: ", convertion(degrees))


#ex2
import math

def calc(base1, base2, height):
    return 0.5 * (base1 + base2) * height

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = float(calc(base1, base2, height))

print("Expected Output: ", area)


#ex3
import math

def calc(n, l):
    a = n * l**2
    b = 4 * math.tan(math.pi / n)
    return a / b 

n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
area = calc(n, l)
print("The area of the polygon is: ", area)


#ex4
import math

def calc(length, height):
    return length * height

length = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
area = calc(length, height)
print("Expected Output: ", area)

