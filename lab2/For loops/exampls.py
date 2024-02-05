#1exm
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2exm
for x in "banana":
  print(x)

#3exm
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#4exm
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#5exm
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#6exm
for x in range(6):
  print(x)

#7exm
for x in range(2, 6):
  print(x)

#exm8
for x in range(2, 30, 3):
  print(x)

#9exm
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#exm10
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#11exm
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#12exm
for x in [0, 1, 2]:
  pass
