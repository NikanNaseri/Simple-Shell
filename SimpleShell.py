import os

def pwd():
    print(os.getcwd())
    return
def ls():
    items = os.listdir()
    for i in items:
        print(i)
    return
def cd(path):
    try:
        os.chdir(path)
    except FileNotFoundError:
        print("Directory not found!")
    return
def ni(file_name):
    try:
        with open(file_name, 'x') as file:                 # make file if it doesn't exist or else run error
            pass
    except FileExistsError:
        print("File already exists!")
    return
def mkdir(directory_name):
    try:
        os.mkdir(directory_name)
    except FileExistsError:
        print("Directory already exists")
def rm(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("File not found!")
    except IsADirectoryError:
        print("Cannot remove directory. Use rmdir instead!")
    except PermissionError:
        print("Permission denied.")
    return
def rmdir(directory_name):
    try:
        os.rmdir(directory_name)
    except FileNotFoundError:
        print("Directory not found!")
    except OSError:
        print("Directory is not empty")
    return
def cat(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found!")
    return

while True:
    os.system("cls")
    user_order = input()
    print()
    if user_order == "exit":
        break
    elif user_order == "pwd":
        pwd()
    elif user_order == "ls":
        ls()
    elif "cd" in user_order:
        user_order = user_order.split()
        user_order.pop(0)                              # removing the word 'cd' from the begining of the path
        path = " ".join(user_order)
        cd(path)
    elif "ni" in user_order:
        user_order = user_order.split()
        user_order.pop(0)                              
        file_name = " ".join(user_order)
        ni(file_name)
    elif "mkdir" in user_order:
        user_order = user_order.split()
        user_order.pop(0)                              
        directory_name = " ".join(user_order)
        mkdir(directory_name)
    elif "rm" in user_order and user_order.split()[0] == "rm":
        user_order = user_order.split()
        user_order.pop(0)                              
        file_name = " ".join(user_order)
        rm(file_name)
    elif "rmdir" in user_order:
        user_order = user_order.split()
        user_order.pop(0)                              
        directory_name = " ".join(user_order)
        rmdir(directory_name)
    elif "cat" in user_order:
        user_order = user_order.split()
        user_order.pop(0)                              
        file_name = " ".join(user_order)
        cat(file_name)
    else:
        print("Wrong order!")
    print("-" * 30)
    print("\nPress Enter...")
    input()
