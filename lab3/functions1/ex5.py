from itertools import permutations 
def prinnper(input_str):
    for i in permutations(input_str):
        print(''.join(i))

prinnper("ABC") 
