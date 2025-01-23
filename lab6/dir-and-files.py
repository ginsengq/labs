import os

#ex1
def list_directories_and_files(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

def list_all_directories_and_files(path):
    print("All Directories and Files:")
    for root, directories, files in os.walk(path):
        for directory in directories:
            print(os.path.join(root, directory))
        for file in files:
            print(os.path.join(root, file))

specified_path = input("Input path: ")
list_directories_and_files(specified_path)
print("\n")
list_all_directories_and_files(specified_path)


#ex2
def check_path_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return
    
    print(f"Path '{path}' exists.")

    if os.access(path, os.R_OK):
        print("Readable: Yes")
    else:
        print("Readable: No")

    if os.access(path, os.W_OK):
        print("Writable: Yes")
    else:
        print("Writable: No")

    if os.access(path, os.X_OK):
        print("Executable: Yes")
    else:
        print("Executable: No")

specified_path = input("Input path: ")
check_path_access(specified_path)


#ex3
def test_path(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

specified_path = input("Input path: ")
test_path(specified_path)


#ex4
def count_lines(filename):
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
    return line_count

file_path = input("Input path to file: ")
lines = count_lines(file_path)
print(f"Number of lines in '{file_path}': {lines}")


#ex5
def write_list_to_file(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')

lst = input("Input: ")
items = list(map(int, lst.split()))
file_path = input("Input path to file: ")
write_list_to_file(items, file_path)
print(f"The list has been written to '{file_path}'.")


#ex6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("This is file " + filename)

generate_files()


#ex7
def copy_file(source, destination):
    with open(source, 'r') as source:
        with open(destination, 'w') as destination:
            destination.write(source.read())

source = input("Path to source file: ")
destination = input("Path to destination file: ")

copy_file(source, destination)
print(f"Contents of '{source}' have been copied to '{destination}'.")


#ex8
def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print(f"File '{file_path}' has been deleted.")
        else:
            print(f"No write access to '{file_path}'. Unable to delete.")
    else:
        print(f"File '{file_path}' does not exist.")

specified_path = input("Input path: ")
delete_file(specified_path)





