import math 

def dist_formula(x1,y1,x2,y2):
    ''' returns the distance between two sets of coordinates
    
    >>> dist_formula(8,2,3,2)
    5.0
    
    >>> dist_formula(3,7,5,7)
    2.0
    
    >>> dist_formula(2,3,4,5)
    2.83
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
    -2 / 3
    
    >>> slope(0,42,0,5)
    undefined
    
    >>> slope(42,0,5,0)
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
        m = (f"{rise} / {run}")
        print(m)
        
def point_slope(x1,y1,m):
    '''uses point slope form

    >>> point_slope(-4,7, 1/4)
    y = 1/4x + 8
    '''
    s = m * x1
    b = (-y1) + s
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
        x1 = int(input('x1: '))
        y1 = int(input('y1: '))
        x2 = int(input('x2: '))
        y2 = int(input('y2: '))
        dist_formula(x1,y1,x2,y2)
    if n == '2':
        a = int(input('a: '))
        b = int(input('b: '))
        pythagorean_theorem(a,b)
    if n == '3':
        multiply_binomials()
    if n == '4':
        slope()        


if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()


print()