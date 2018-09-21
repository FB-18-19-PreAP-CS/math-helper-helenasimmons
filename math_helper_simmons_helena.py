import math 

def dist_formula(x1,y1,x2,y2):
    ''' returns the distance between two sets of coordinates
    
    >>> dist_formula(8,2,3,2)
    5.0
    
    >>> dist_formula(3,7,5,7)
    2.0
    
    >>> dist_formula(2,3,4,5)
    2.83
    
    >>> dist_formula(10,0,0,4)
    10.77
    
    >>> dist_formula(-7,-2,6,9)
    17.03
    '''
    dist = math.sqrt((x1-x2)**2+(y1-y2)**2)
    dist= round(dist,2)
    print(dist)
    
def pythagorean_theorem(a,b):
    ''' pythagorean theorem. Gives back the value of c. 
    
    >>> pythagorean_theorem(-3,4)  
    A side of a triangle shouldn't be negative or zero!
    
    >>> pythagorean_theorem(0,24) 
    A side of a triangle shouldn't be negative or zero!
    
    >>> pythagorean_theorem(361,42) 
    363.44
    
    >>> pythagorean_theorem(65,0.2)
    65.0
    
    >>> pythagorean_theorem(7,4412)
    4412.01
    '''
    if a <= 0 or b <= 0:
        print('A side of a triangle shouldn\'t be negative or zero!')
    elif a != 0 and b != 0:
        c = math.sqrt(a**2 + b**2)
        c = round(c,2)
        print(c)

def multiply_binomials(a1,b1,a2,b2):
    '''multiplies two binomials into a trinomial.
    
    >>> multiply_binomials(3,-5,1,7)
    3x^2 + 16x + -35
    
    >>> multiply_binomials(1,2,1,-3)
    1x^2 + -1x + -6
    
    >>> multiply_binomials(1,1,2,-5)
    2x^2 + -3x + -5
    
    >>> multiply_binomials(1,10,1,10)
    1x^2 + 20x + 100
    
    >>> multiply_binomials(6,7,6,-7)
    36x^2 + 0x + -49
    '''
    f = a1 * a2
    o = a1 * b2
    i = b1 * a2
    l = b1 * b2
    sum = o+i
    ans = (f"{f}x^2 + {sum}x + {l}")
    print(ans)
    
def slope(x1,y1,x2,y2):
    '''gives the slope between two points. 
    
    >>> slope(-1,-3,2,-5)
    -0.67

    >>> slope(0,42,0,5)
    undefined
    
    >>> slope(42,0,5,0)
    0
    
    >>> slope(1,-19,-2,-7)
    -4.0
    
    >>> slope(19,3,20,3)
    0
    '''
    rise = (y2-y1)
    run = (x2-x1)
    if run == 0:
        m = "undefined"
        print(m)
    elif rise == 0:
        m = 0
        print(m)
    elif run != 0 and rise != 0:
        m = round(rise/run,2)
        print(m)
        
def slope_intercept_form(x1,y1,m):
    '''uses point slope form

    >>> slope_intercept_form(-4,7, 1/4)
    y = 0.25x + 8.0
    
    >>> slope_intercept_form(3,7,12)
    y = 12x + -29
    
    >>> slope_intercept_form(4,5,9)
    y = 9x + -31
    
    >>> slope_intercept_form(-200,42, -2/13)
    y = -0.15x + 11.23
    
    >>> slope_intercept_form(1,1,1)
    y = 1x + 0
    '''
    s = m * -x1
    b = y1 + s
    m = round(m,2)
    b = round(b,2)
    o = (f'y = {m}x + {b}')
    print(o)
        
def main():
    print('Hello there!')
    print('What do you want to do?')
    print()
    print('1. Distance Formula')
    print('2. Pythagorean Theorem')
    print('3. Multiply binomials in the form of (ax + b)(cx + d)')
    print('4. Find the slope between two points.')
    print('5. Point Slope Form')
    print()
    n = input('> ')
    if n == '1':
        print()
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))
        x2 = int(input('x2: '))
        y2 = int(input('y2: '))
        dist_formula(x1,y1,x2,y2)
    if n == '2':
        print()
        a = int(input('a: '))
        b = int(input('b: '))
        pythagorean_theorem(a,b)
    if n == '3':
        a1 = int(input('a1: '))
        b1 = int(input('b1: '))
        a2 = int(input('a2: '))
        b2 = int(input('b2: '))
        print()
        multiply_binomials(a1,b1,a2,b2)
    if n == '4':
        print()
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))
        x2 = int(input('x2: '))
        y2 = int(input('y2: '))
        slope(x1,y1,x2,y2)
    if n == '5':
        print()
        print('Please enter your coordinates and the slope.')
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))
        m = int(input('m: '))
        slope_intercept_form(x1,y1,m)
    elif n != '1' or n != '2' or n != '3' or n != '4' or n != '5':
        print('That was not one of the listed choices!')


if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()


print()