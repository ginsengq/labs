#ex1
import math

def operations(numbers):
    return math.prod(numbers)
    
lst = input("Input: ")
numbers = list(map(int, lst.split()))

print(f"Result: '{operations(numbers)}'")


#ex2
def counting(string):
    up = 0
    low = 0
    
    for char in string:
        if char.isupper():
            up += 1
        elif char.islower():
            low += 1
    
    return up, low
    
string = input("Input: ")
up_count, low_count = counting(string)
print(f"Number of upper chars: {up_count}")
print(f"Number of lower chars: {low_count}")


#ex3
def palindrome(string):
    string = string.lower()
    return string == string[::-1]

string = input("Input: ")

if palindrome(string):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


#ex4
import time
import math

def calculations(number, millisec):
    time.sleep(millisec/1000)
    root = math.sqrt(number)
    return root

number = int(input("Input a number: "))
millisec = int(input("Input a millisec: "))
print(f"Square root of {number} after {millisec} miliseconds is {calculations(number, millisec)}")


#ex5
def returning(tpl):
    return all(tpl)

string = input("Input: ")
tpl = tuple(map(lambda x: x == "True", string.split()))
print(f"Output: {returning(tpl)}")