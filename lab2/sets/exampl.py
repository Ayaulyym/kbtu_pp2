#1exm
myset = {"apple", "banana", "cherry"}

#2exm
thisset = {"apple", "banana", "cherry"}
print(thisset)

#3exm
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#4exm
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#5exm
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#6exm
set1 = {"abc", 34, True, 40, "male"}

#7exm
myset = {"apple", "banana", "cherry"}
print(type(myset))

#exm8
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#9exm
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#exm10
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#11exm
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#12exm
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#13exm
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

#14exm
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

#15exm
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

#exm16
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#17exm
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#18exm
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#19exm
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

#20exm
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)

#exm21
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

#22exm
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)
