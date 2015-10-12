#Problem 12
#dummy comment for test2

def triangle(end):
        newNums = [x for x in range(1,end+1)]
        sum = 0
        for num in newNums:
                sum += num
        return sum

def factor(number):
        factors = []
        for i in range(1,(number+1)):
                if number%i == 0:
                        factors.append(i)
        return factors

numFactors = 0
i = 1
max = 1

while 1:
        triNum = triangle(i)            #Calculate the next triangular number
        factors = factor(triNum)        #Factor that number
        if len(factors) > max:
                max = len(factors)
                print str(max) + " (" + str(i) + "th triangle number, which is " + str(triNum) + ")"
        if len(factors) > 500:          #How many factors are there? if >500, we are done
                break
        i += 1

print triNum

        
                        
