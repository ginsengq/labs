#ex1
def gen(N):
    for i in range(1, N+1):
        yield i**2

N = int(input("Input: "))
squares = gen(N)
for square in squares:
    print(square)


#ex2
def gen(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i

n = int(input("Input: "))
evens = gen(n)
res = ", ".join(str(even) for even in evens)
print(res)


#ex3
def operations(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Input: "))
for num in operations(n):
    print(num)


#ex4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2

a = int(input("Input a: "))
b = int(input("Input b: "))
for square in squares(a, b):
    print(square)


#ex5
def down(n):
    while n >= 0:
        yield n 
        n -= 1

n = int(input("Input: "))
for num in down(n):
    print(num)
