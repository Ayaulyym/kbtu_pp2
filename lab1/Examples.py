#home
print("Hello, World!")

#intro
print("Hello, World!")

#getstarted
print("Hello, World!")

#SYNTAX
 #exm1
if 5 > 2:
  print("Five is greater than two!")
 
 #exm2
SyntaxError
if 5 > 2:
  print("Five is greater than two!")
 
 #exm3
if 5 > 2:
  print("Five is greater than two!") 
if 5 > 2:
         print("Five is greater than two!")
 
 #exm4
SyntaxError
if 5 > 2:
  print("Five is greater than two!")
  print("Five is greater than two!")

#COMMENTS
 #exm1
 #This is a comment
  print("Hello, World!")
 
 #exm2
print("Hello, World!") #This is a comment

 #exm3
 #print("Hello, World!")
print("Cheers, Mate!")

 #exm4
 #This is a comment
 #written in
 #more than just one line
print("Hello, World!")

 #exm5
"""
 This is a comment
 written in
 more than just one line
 """
print("Hello, World!")

#VARIABLES
 #exm1
x = 5
y = "John"
print(x)
print(y)

 #exm2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

 #exm3
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

 #exm4

x = 5
y = "John"
print(type(x))
print(type(y))

 #exm5
x = "John"
 # is the same as
x = 'John'

 #exm6
a = 4
A = "Sally"
 #A will not overwrite a

 #exm7
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

 #exm8
myvar = "John"
 #my-var = "John"
 #my var = "John"

#exm9
 x, y, z = "Orange", "Banana", "Cherry"
 print(x)
 print(y)
 print(z)

 #exm10
 x = y = z = "Orange"
 print(x)
 print(y)
 print(z)
 
 #exm11
 fruits = ["apple", "banana", "cherry"]
 x, y, z = fruits
 print(x)
 print(y)
 print(z)

 #exm12
 x = "Python is awesome"
 print(x)


 #exm13
 x = "Python"
 y = "is"
 z = "awesome"
 print(x, y, z)

 #exm14
 x = "Python "
 y = "is "
 z = "awesome"
 print(x + y + z)
 
 #exm15
 x = 5
 y = 10
 print(x + y)

 #exm16
 x = 5
 y = "John"
 print(x + y)

 #exm17
 x = 5
 y = "John"
 print(x, y)

 #exm18
 x = 5
 y = "John"
 print(x, y)

 #exm19
 x = "awesome"

 def myfunc():
   x = "fantastic"
   print("Python is " + x)

 myfunc()

 print("Python is " + x)

 #exm20
 def myfunc():
   global x
   x = "fantastic"

 myfunc()

 print("Python is " + x)

 #exm21
 x = "awesome"

 def myfunc():
   global x
   x = "fantastic"

 myfunc()

 print("Python is " + x)


#Datatypes
 #exm1
 x = 5
 print(type(x))
 
#NUMBERS

 #exm1
 x = 1    # int
 y = 2.8  # float
 z = 1j   # complex

 #exm2
 print(type(x))
 print(type(y))
 print(type(z))


 #exm3
 x = 1
 y = 35656222554887711
 z = -3255522

 print(type(x))
 print(type(y))
 print(type(z))
 
 #exm4
 x = 1.10
 y = 1.0
 z = -35.59

 print(type(x))
 print(type(y))
 print(type(z))

 #exm5
 x = 1    # int
 y = 2.8  # float
 z = 1j   # complexx = 3+5j
 y = 5j
 z = -5j

 print(type(x))
 print(type(y))
 print(type(z))

 #exm6
 x = 1    # int
 y = 2.8  # float
 z = 1j   # complex

 #convert from int to float:
 a = float(x)

 #convert from float to int:
 b = int(y)

 #convert from int to complex:
 c = complex(x)

 print(a)
 print(b)
 print(c)

 print(type(a))
 print(type(b))
 print(type(c))


 #exm7
 import random

 print(random.randrange(1, 10))
 
#CASTING
#exm1
 x = int(1)   # x will be 1
 y = int(2.8) # y will be 2
 z = int("3") # z will be 3

 #exm2
 x = float(1)     # x will be 1.0
 y = float(2.8)   # y will be 2.8
 z = float("3")   # z will be 3.0
 w = float("4.2") # w will be 4.2

 
 #exm3
 x = str("s1") # x will be 's1'
 y = str(2)    # y will be '2'
 z = str(3.0)  # z will be '3.0'


#STRING
 #exm1
 print("Hello")
 print('Hello')


 #exm2
 a = "Hello"
 print(a)

 #exm3
 a = """Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
 sed do eiusmod tempor incididunt
 ut labore et dolore magna aliqua."""
 print(a)
 
 #exm4
 a = '''Lorem ipsum dolor sit amet,
 consectetur adipiscing elit,
 sed do eiusmod tempor incididunt
 ut labore et dolore magna aliqua.'''
 print(a)

 #exm5
 a = "Hello, World!"
 print(a[1])

 #exm6
 for x in "banana":
  print(x)

 #exm7
  txt = "The best things in life are free!"
 if "free" in txt:
   print("Yes, 'free' is present.")

 #exm8
 #txt = "The best things in life are free!"
 if "expensive" not in txt:
   print("No, 'expensive' is NOT present.")


 #exm9
   b = "Hello, World!"
 print(b[2:5])


 #exm10
 b = "Hello, World!"
 print(b[2:])

 #exm11
 b = "Hello, World!"
 print(b[-5:-2])

 #exm12 
 a = "Hello, World!"
 print(a.upper())

 #exm13
 a = "Hello, World!"
 print(a.lower())

 #exm14
 a = " Hello, World! "
 print(a.strip()) # returns "Hello, World!"

 #exm15
 a = "Hello, World!"
 print(a.replace("H", "J"))

 #exm16
 a = "Hello" 
 b = "World"
 c = a + b
 print(c)

 #exm17
 a = "Hello"
 b = "World"
 c = a + " " + b
 print(c)

 #exm18
 age = 36
 txt = "My name is John, I am " + age
 print(txt)


 #exm19
 age = 36
 txt = "My name is John, and I am {}"
 print(txt.format(age))

 #exm20
 quantity = 3
 itemno = 567
 price = 49.95
 myorder = "I want {} pieces of item {} for {} dollars."
 print(myorder.format(quantity, itemno, price))

 #exm21
 quantity = 3
 itemno = 567
 price = 49.95
 myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
 print(myorder.format(quantity, itemno, price))

 #exm22
 #txt = "We are the so-called "Vikings" from the north."

