#Problem 12
#dummy comment for test

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

result = triangle(naturalNumbers, 3)
print "\n"
print result
