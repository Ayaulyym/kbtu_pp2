from functools import reduce

def multiplyList(s):
    result = reduce(lambda x, y: x * y, s)
    return result