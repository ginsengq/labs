#ex1
class Metamorphosis():
    def getString(self):
        self.string = input()

    def printString(self):
        print(self.string.upper())

stringManipulator = Metamorphosis()
stringManipulator.getString()
stringManipulator.printString()


#ex2
class Shape():
    def g(self):
        print("Input: ")
        self.input_val = int(input())

class Square(Shape):
    def __init__(self):
        super().__init__()
        self.leng = None

    def area(self):
        return self.leng ** 2
    
    def g(self):
        super().g()
        self.leng = self.input_val

ar = Square()
ar.g()
res = ar.area()
print("Area: ", res)


#ex3
class Rectangle():
    def __init__(self):
        self.len = int(input("L: "))
        self.width = int(input("W: "))

class Shape(Rectangle):
    def __init__(self):
        super().__init__()
    
    def arr(self):
        self.area= self.len * self.width
        return self.area
    
ar = Shape()
res = ar.arr()
print("Output: ", res)


#ex4
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def show(self):
        print(str(self.x) + ";" + str(self.y))

    def move(self):
        global x, y
        x = int(input("Change x: "))
        y = int(input("Change y: "))

    def dist(self):
        self.r = int(input("From x: "))
        self.t = int(input("From y: "))
        c = ((self.x-self.r)**2 + (self.y-self.t)**2)**0.5
        return c
    
x = 4
y = 9
point = Point(x,y)
point.show()
point.move()
print(x,y)
res=point.dist()
print(res)


#ex5
class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, a):
        self.balance += a
        print(f"New balance: {self.balance}")
    
    def withdraw(self, subt):
        if subt <= self.balance:
            self.balance -= subt
            print(f"New balance: {self.balance}")
        else:
            print("Balance is too low.")

acc = Account(owner = "Kiko", balance = 22000)

acc.withdraw(500)
acc.withdraw(500000)

acc.deposit(1000)
acc.deposit(300)


#ex6
def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

arr = [11,3 ,4 ,67,55,9, 7, 99, 87, 53]

prime_nums = list(filter(lambda x: is_prime(x), arr))
print(prime_nums)