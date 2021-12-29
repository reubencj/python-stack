'''
Basic - Print all integers from 0 to 150.
Multiples of Five - Print all the multiples of 5 from 5 to 1,000
Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum 
    and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
'''

#basic
for x in range(151):
    print(x)

#Multiples of Five

for x in range(5,1001):
    print(x*5)

#Counting, the Dojo Way

for x in range(1,101): 
    if x % 10 == 0:
        print("coding dojo")
    elif x % 5 == 0:
        print("coding")
    else:
        print(x)

#Whoa. That Sucker's Huge
oddSum = 0
for x in range(0,500000):
    if x % 2 != 0:
        oddSum += x
print(oddSum)


#Countdown by Fours

for x in range(2018,-1,-4):
    print(x)

#Flexible Counter

lowNum = 2
highNum = 100
mult = 3

for x in range(lowNum,highNum+1):
    if x % 3 == 0:
        print(x)