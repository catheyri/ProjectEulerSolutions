def find_factor(x):
    for div in range(2, 1000000):
        if ((x%div)==0):
            x //= div
            if (x == 1 or x == div):
                print(div)
                return div

find_factor(600851475143)
