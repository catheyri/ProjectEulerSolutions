import math

def is_prime(i):
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            return 0
    return 1

def nth_prime(n):
    #going to tally 2 as the first one and not test for it, start with 3
    numPrimes = 1
    i = 3
    while (1):
        if (is_prime(i)):
            numPrimes += 1
            if (numPrimes == n):
                return i
        #only need to check odd values
        i += 2

print(nth_prime(10001))


