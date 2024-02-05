#1exm
mytuple = ("apple", "banana", "cherry")

#2exm
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#3exm
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#4exm
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#5exm
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#6exm
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#7exm
tuple1 = ("abc", 34, True, 40, "male")

#exm8
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#9exm
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])


#exm10
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

#11exm
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#12exm
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

#13exm
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#14exm
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#15exm
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#exm16
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

#17exm
fruits = ("apple", "banana", "cherry")

#18exm
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#19exm
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#20exm
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#exm21
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#22exm
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#23exm
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#24exm
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#25exm 
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
