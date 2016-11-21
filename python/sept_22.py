#!/usr/bin/python
'''
Define the functions div by 400,100,4
Create a function to check if it is a leap year by following
'''

'''
The way I would have done it: I like the modularity

def divisibleBy100(num):
    return (num % 100) == 0

def divisibleBy400(num):
    return (num % 400) == 0

def divisibleBy4(num):
    return (num % 4) == 0

def isALeapYear(year):
    return divisibleBy400(year) or (not divisibleBy100(year) and divisibleBy4(year))
'''

def isALeapYear(year):
    if year % 400 == 0:
        return True
    else:
        if (year % 100 != 0 and year % 4 == 0):
            return True
        else:
            return False

'''
tests
'''

def loopUser():
    year = raw_input('enter a year: \n')
    check = isALeapYear(float(year))
    if check:
        print 'yep,', year, 'is a leap year'
    else:
        print 'nope,', year, 'is not a leap year'
    goOn = raw_input('Continue y/n: \n')
    if (goOn == 'y'):
        loopUser()
    else:
        print 'cya l8r alig8r'
loopUser()

#print '2016', isALeapYear(2016)
#print '1900', isALeapYear(1900)
#print '2000', isALeapYear(2000)
#print '2015', isALeapYear(2015)
