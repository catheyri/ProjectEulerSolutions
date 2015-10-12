#Problem 12
#dummy comment for test2

end = 10

naturalNumbers = [x for x in range(1,end+1)]

print naturalNumbers

def triangle(nums, index):
        newNums = nums[0:index]
        sum = 0
        for num in newNums:
                print num
                sum += num
        return sum

result = triangle(naturalNumbers, 7)
print "\n"
print result

def factor(number):
        factors = []
        for i in range(1,(number/2)+1):
                if number%i == 0:
                        factors.append(i)
                        number = number/i
                        print i
        return factors

primeFactors = factor(result)
print primeFactors
print len(primeFactors)
        
                        
