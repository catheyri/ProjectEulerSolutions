import math

def find_triple(rng):
    #largest number satisfying a+b+c = range
    #would be 1 + 2 + number, so subtract the 1+2
    rng = rng - 3
    for i in range(1, rng+1):
        for j in range(i+1, rng+1):
            k = math.sqrt(i**2 + j**2)
            #if it's a whole number and the sum is <rng
            if k%1 == 0:
                if i+j+int(k) == rng+3:
                    return i*j*int(k)
    return [0, 0, 0]

print(find_triple(1000))
