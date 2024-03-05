filefirst = open("file1.txt", "r")

filesecond = open("file2.txt", "w")

filesecond.write(filefirst.read())

filefirst.close()
filesecond.close()