#1exm
#If statement:
a = 33
b = 200
if b > a:
  print("b is greater than a")

#2exm
#If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
  print("b is greater than a") # you will get an error

#3exm
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#4exm
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#5exm
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#6exm
if a > b: print("a is greater than b")

#7exm
a = 2
b = 330
print("A") if a > b else print("B")

#exm8
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#9exm
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#exm10
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#11exm
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#12exm
  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#13exm
a = 33
b = 200

if b > a:
  pass


