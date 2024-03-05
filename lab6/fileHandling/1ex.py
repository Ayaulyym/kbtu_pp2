import os

def listdir(path):

    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)


    print("\nFiles:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)


    print("\nAll Directories and Files:")
    for root , dirs , files in os.walk(path):
        for DiR in dirs:
            print(os.path.join(root, DiR))
        for FilE in files:
            print(os.path.join(root, FilE))

path = ""

listdir(path)