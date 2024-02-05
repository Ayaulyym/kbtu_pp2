#1exm
print(10 > 9)
print(10 == 9)
print(10 < 9)

#2exm
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3exm
print(bool("Hello"))
print(bool(15))

#4exm
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#5exm
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#6exm
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#7exm
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#exm8
def myFunction() :
  return True

print(myFunction())

#9exm
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#exm10
x = 200
print(isinstance(x, int))


