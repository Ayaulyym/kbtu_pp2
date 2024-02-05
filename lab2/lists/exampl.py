#1exm
thislist = ["apple", "banana", "cherry"]
print(thislist)

#2exm
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

#3exm
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#4exm
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

#5exm
list1 = ["abc", 34, True, 40, "male"]

#6exm
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#7exm
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#exm8
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#9exm
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#exm10
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#11exm
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

#12exm
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#13exm
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#14exm
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#15exm
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#exm16
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#17exm
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#18exm
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#19exm
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#20exm
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#exm21
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#22exm
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

#23exm
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

#24exm
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#25exm all list delete
thislist = ["apple", "banana", "cherry"]
del thislist

#26exm
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#27exm
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#28exm
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#29exm 
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#30exm
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#31exm
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#32exm
newlist = [x for x in fruits if x != "apple"]

#33exm
newlist = [x for x in fruits]

#34exm
newlist = [x.upper() for x in fruits]

#35exm
newlist = ['hello' for x in fruits]

#36exm
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#37exm
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#38exm
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

#39exm
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#40exm
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#41exm
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#42exm
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

