import math

def is_prime(i):
    for j in range(2, int(math.sqrt(i))+1):
        if i%j == 0:
            return 0
    return 1

def sum_primes(rng):
    #skip 2, we know it's prime and it just fucks stuff up
    sum = 2
    for i in range(3, rng+1):
        if (is_prime(i)):
            sum = sum + i
    return sum

print(sum_primes(2000000))
            
