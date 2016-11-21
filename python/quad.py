import cmath

'''
-- First gets the inputs
-- Then define function for quadratic formula : returns the value
-- Use the function and run it
'''

i1 = float(input('Enter a: '))
i2 = float(input('Enter b: '))
i3 = float(input('Enter c: '))

def quad (a,b,c):
    d = (b**2) - (4*a*c)
    if (d < 0):
        return ['not valid input']
    opt1 = (-b-cmath.sqrt(d))/(2*a)
    opt2 = (-b+cmath.sqrt(d))/(2*a)
    return [opt1, opt2]

print quad(i1,i2,i3)
