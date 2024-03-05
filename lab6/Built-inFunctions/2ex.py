Lett = input()

upper = sum( map(lambda x: x.isupper(), Lett))
lower = sum( map(lambda x: x.islower(), Lett))
print(upper, lower)