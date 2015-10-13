def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

i = 0
num = 0
total = 0
while(1):
    num = fib(i)
    if (num >= 4000000): break
    if ((num%2)==0):
        total = total + num
    i = i+1

print(total)
