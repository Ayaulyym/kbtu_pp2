def Line(S):
    t = 0
    for i in S:
        t += 1
    return t

file = open("file.txt", "r")
print( Line(file))
file.close()