def pal(j):
    for i in range (999, 100, -1):
            p = str(i*j)
            if p == p[::-1]:
                return i*j
    return 0

largest = 0
for j in range (999, 100, -1):
    x = pal(j)
    if x > largest:
        largest = x

print(largest)
