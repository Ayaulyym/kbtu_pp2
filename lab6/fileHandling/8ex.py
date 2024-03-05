import os

path = ""

def ex(path):
    if os.path.exists(path):
        os.remove(path)

        return "file you want to delete"
    else:
        return "File is does not exist"
    
print(ex(path))
    