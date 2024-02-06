def filter_prime(numbers):
    list_num = [int(i) for i in numbers.split()]
    def isPrime(num):
        for i in range(2, num//2+1):
            if num%i == 0:
                return False
        return True
        
    return [x for x in list_num if isPrime(x)]

print(filter_prime("1 2 3 4 5 6 7 8 9 10"))