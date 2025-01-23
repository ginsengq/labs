#ex1
grams = float(input())
def conversion(grams):
    return 28.3495231 * grams
print(conversion(grams))


#ex2
F = float(input())
def conversion(F):
    return (5 / 9) * (F - 32)
print(conversion(F))


#ex3
def solve(nheads, nlegs):
    for i in range(1, nheads+1):
        if i * 4 + (nheads - i) * 2 == nlegs:
            return i
        
heads,legs = 35, 94
rab = int(solve(heads, legs))
chick = heads - rab
print("Rabbits: ", rab, "Chickens: ", chick)


#ex4
import math
nums = input()
list = []
for i in nums.split():
    list.append(int(i))
def filter_prime(nums):
    primes = []
    for num in nums:
        if num > 1:
            is_prime = True
            for i in range(2, math.isqrt(num) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
    return primes

print(filter_prime(nums))


#ex5
def permutations(input_str, cur_per= ""):
    if not input_str:
        print(cur_per)
        return

    for i in range(len(input_str)):
        cur_char = input_str[i]

        rem_chars = input_str[:i] + input_str[i + 1:]

        permutations(rem_chars, cur_per + cur_char)

n = input("Input: ")
permutations(n)


#ex6
def reverse_words():
    words = s.split()
    rev_words = words[::-1]
    rev = ' '.join(rev_words)
    return rev 

s = input()
print(reverse_words(s))


#ex7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            print("True")
            return 0
        print("False")
        return 0

'''has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False'''


#ex8
def spy_game(nums):
    res = 0
    for i in range(len(nums)):
        if res < 3 and nums[i] == 0:
            res += 1
        elif nums[i] == 7:
            res += 1
    
    if res == 3:
        print("True")
    else:
        print("False")

'''spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False'''


#ex9
def volume(r):
    v = 4/3 * 3,14 * r**3
    return v

r = float(input())
print(volume(r))


#ex10
def uniques(nums):
    uniq = []
    for i in nums:
        if i not in uniq:
            uniq.append(i)
    return uniq

nums_str = input()
nums_list = nums_str.split()
uniq = uniques(nums)
nums = [int(num) for num in nums_list]
print(uniq)


#ex11
def palindrome(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            print("Not palindrome")
            return 0
    print("Palindrome")
    return 0

s = input()
palindrome(s)


#ex12
def histogram(n):
    for i in range(len(n)):
        r = ""
        for j in range(n[i]):
            r += "*"
        print(r)

n = input()
histogram(n)


#ex13
from random import randint

def rand(x, y):
    if x != y:
        return False
    return True

y = randint(1, 20)
print("Hello! What is your name?")
name = input()
game = 0

print("Well, {name}, I am thinking of a number between 1 and 20.")
print("Take a guess.")
x = int(input())

while not r(x, y):
    game += 1
    if x < y:
        print("Your guess is too low.")
    else: 
        print("Your guess is too high.")
    print("Take a guess.")
    x = int(input())

print("Good job, {name}! You guessed my number in {game} guesses!")


def rev(s):
    user_string = s.split()
    for words in range(len(user_string)):
        words[::-1]
    return user_string

s = str(input())
rev(s)