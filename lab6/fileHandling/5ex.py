s = [1,2,3,4,5]

with open("file.txt", "w") as S:
    for i in s:
        S.write(str(i)+" ")