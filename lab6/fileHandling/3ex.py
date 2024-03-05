import os

def PATH(path):
    if os.path.exists(path):
        print(f" The path exists ")
        filename = os.path.basename(path)
        dir = os.path.dirname(path)
        print(f" Filename: {filename}")
        print(f" Directory: {dir}")
        
    else:
        print("The path does not exist ")

path = input()
PATH(path)