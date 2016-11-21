from datetime import date
# need library for relative responses

# something nice to say
greeting = 'Hey Mr.P'
cheesyGreeting = 'Clear skies today, huh? Oh right! it\'s DOOMSDAY (algorithm)'
wantsCheesy = raw_input('want the cheesy greeting? (y/n):\n')
if wantsCheesy == 'y':
    print cheesyGreeting
else:
    print greeting

def getDoomsdayFromYear(year):
    year = str(year)
    lastTwoDigits = int(year[-2:])
    #print 'lastTwoDigits', lastTwoDigits
    twelveIntoLastTwo = int(lastTwoDigits / 12)
    #print 'howmany12intoit', twelveIntoLastTwo
    yearModulo12 = lastTwoDigits%12
    #print 'modulo12', yearModulo12
    fourIntoCalcTwo = int(yearModulo12/4)
    #print 'fitsHowManyTime4intoCalc2', fourIntoCalcTwo
    anchor = getAnchorDayFromYear(year)
    #print 'century anchor', anchor
    sumOfAll = (twelveIntoLastTwo + yearModulo12 + fourIntoCalcTwo + anchor)
    #print sumofall
    return sumOfAll % 7

def getAnchorDayFromYear(year):
    firstpart = int(str(year)[:-2])
    remainder = firstpart % 4
    anchordays = [2, 0, 5, 3]
    return anchordays[remainder]

#print getAnchorDayFromYear(2016)

#print getDoomsdayFromYear(2016)

def isALeapYear (year):
    def divisibleBy100(num):
        return (num % 100) == 0
    def divisibleBy400(num):
        return (num % 400) == 0
    def divisibleBy4(num):
        return (num % 4) == 0
    return divisibleBy400(year) or (not divisibleBy100(year) and divisibleBy4(year))

def numToDay (num):
    # CONVERT NUM TO DAY
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    return days[num]

def getMonthsDoomsday(month, year):
    # RETURN DOOMSDAY DATE FROM MONTH (YEAR FOR LEAP YEAR)
    # added 0 in the beggining for easy in & out. no substracting -1
    # index is correlated to doomsday of that month
    doomsdays = [0, 3, 21, 0, 4, 9, 6, 11, 8, 5, 10, 7, 12]
    # Leap year add 1 to february
    if isALeapYear(year) and (month == 2 or month == 1):
        #print 'leap'
        return doomsdays[month] + 1
    else:
        return doomsdays[month]

def getDayFromDate(day, month, year):
    yearsDoomday = getDoomsdayFromYear(year)
    monthsDoomsday = getMonthsDoomsday(month, year)
    # Differnce of dates
    doomandnowdiff = monthsDoomsday - day
    # Difference must be a positive number, my version is check <0 then mult * -1 to get positive
    if doomandnowdiff < 0:
        doomandnowdiff*= -1

    # Add the centuries day to the doomsday
    final = doomandnowdiff + yearsDoomday
    # Mod to get 0-7
    final = final % 7
    #remainder = ((math.fabs(day - monthsDoomsday) % 7) + yearsDoomday) % 7
    return numToDay(final)

#print getDayFromDate(14, 7, 2000)

# LOOP THE FUNCTION SO YOU CAN ENJOY ENDLESS DATES
# and error check with relative responses to today
while True:
    day = -1
    month = -1
    year = -1
    while day<0 or day>31:
        try:
            day = int(raw_input('day: '))
        except ValueError:
            print "Please enter a date between 1 and 31"
    while month<0 or month>12:
        try:
            month = int(raw_input('month: '))
        except ValueError:
            print "Please enter a month between 1 and 12"
    while year<1000:
        try:
            year = int(raw_input('year: '))
        except ValueError:
            print "Please enter a year above 1000"
    today = date.today()
    def isToday():
        print '--> Today is a', getDayFromDate(day, month, year), '<--'
    def isPast():
        print '--> It was a', getDayFromDate(day, month, year), '<--'
    def isFuture():
        print '--> It will be a', getDayFromDate(day, month, year), '<--'

    if today.year<year:
        isFuture()
    elif today.year == year:
        if today.month < month:
            isFuture()
        elif today.month == month:
            if today.day < day:
                isFuture()
            elif today.day == day:
                isToday()
            else:
                isPast()
        else:
            isPast()
    else:
        isPast()
    print '\n'
