def spy_game(nums):
    coout= 0
    for num in nums:
        if num == 0:
            coout += 1
        elif coout >= 2 and num == 7:
            return True
    return False

print(spy_game([1,7,2,0,4,5,0])) 