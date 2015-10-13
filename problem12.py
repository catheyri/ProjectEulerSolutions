#Problem 12

import time
startTime = time.time()

def factor(number):
        factors = []
        for i in range(1,(number+1)):
                if number%i == 0:
                        factors.append(i)
        return factors

numFactors = 0
i = 1
triNum = 0
max = 1

while 1:
        triNum += i                     #Calculate the next triangular number
        factors = factor(triNum)        #Factor that number
        if len(factors) > max:
                max = len(factors)
                print str(max) + " (" + str(i) + "th triangle number, which is " + str(triNum) + ")"
        if len(factors) > 500:          #How many factors are there? if >500, we are done
                break
        i += 1

print triNum
currentTime = time.time()
runTime = currentTime - startTime
print str(runTime) + " seconds" 
        
                        
