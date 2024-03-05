import time
import math

def calc(number, timee):
    time.sleep(timee / 1000) 
    result = math.sqrt(number)
    return result

number, timee = input("by space:").split()
number = int(number)
timee = int(timee)

result = calc(number, timee)
print(f"Square root of {number} after {timee} miliseconds is {result}")
