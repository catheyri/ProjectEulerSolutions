def square_of_sum(j):
    numbers = range(1, j+1)
    if j%2 == 0:
        return (numbers[-1]/2 * (numbers[0]+numbers[-1]))**2
    else:
        #wanted to make it work for odd numbers too
        return ((numbers[-2]/2 * (numbers[0]+numbers[-2]))+numbers[-1])**2

def sum_of_squares(j):
    numbers = range(1, j+1)
    total = 0
    for i in numbers:
        total = total + i**2
    return total

print(square_of_sum(100) - sum_of_squares(100))



