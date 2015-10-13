#Problem 12 - second try

number = 300

def factor(num):
    divisors = []
    for i in range(1,num+1):
        if num%i == 0:
            divisors.append(i)
    return divisors

print factor(number)

#Turns out you only need to search for the factors of the sqrt and then multiply
#that number by 2, (minus 1 if it is a perfect square)
