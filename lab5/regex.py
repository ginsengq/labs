import re

#ex1
def matching(s):
    pattern = r"ab*"
    if re.match(pattern, s):
        return True
    else:
        return False
    
s = input("Input: ")

if matching(s):
    print(f"The '{s}' matches.")
else:
    print(f"The '{s}' does not match.")


#ex2
def matching(s):
    pattern = r"ab{2,3}"
    if re.match(pattern, s):
        return True
    else:
        return False
    
s = input("Input: ")

if matching(s):
    print(f"The '{s}' matches.")
else:
    print(f"The '{s}' does not match.")


#ex3
def matching(s):
    pattern = r"\b[a-z]+_[a-z]+\b"
    if re.match(pattern, s):
        return True
    else:
        return False
    
s = input("Input: ")

if matching(s):
    print(f"The '{s}' matches.")
else:
    print(f"The '{s}' does not match.")


#ex4
def matching(s):
    pattern = r"\b[A-Z][a-z]+\b"
    if re.match(pattern, s):
        return True
    else:
        return False
    
s = input("Input: ")

if matching(s):
    print(f"The '{s}' matches.")
else:
    print(f"The '{s}' does not match.")


#ex5
def matching(s):
    pattern = r"a.*b$"
    if re.match(pattern, s):
        return True
    else:
        return False
    
s = input("Input: ")

if matching(s):
    print(f"The '{s}' matches.")
else:
    print(f"The '{s}' does not match.")


#ex6
def replacing(s):
    pattern = r"[ ,.]"
    replacement = ":"
    return re.sub(pattern, replacement, s)

s = input("Input: ")
print("Result: ", replacing(s))


#ex7
def snaketocamel(text):
    text = text.lower()
    pattern = "_(.)"

    replace_f = lambda m: m.group(1).upper()
    camel = re.sub(pattern, replace_f, text)
    return camel

text = input("Input: ")
print(f"Result: '{snaketocamel(text)}'")


#ex8
def splitting(text):
    subtexts = re.findall("[A-Z][^A-Z]*", text)
    return subtexts

text = input("Input: ")
print(f"Result: '{splitting(text)}'")


#ex9
def insertting(text):
    new = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return new

text = input("Input: ")
print(f"Result: '{insertting(text)}'")


#ex10
def cameltosnake(text):
    snake = ''
    for char in text:
        if char.isupper():
            snake += '_' + char.lower()
        else:
            snake += char
    return snake.lstrip('_')

text = input("Input: ")
print(f"Result: '{cameltosnake(text)}'")