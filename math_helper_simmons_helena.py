import math 
    
def vertex_form_to_trinomial(a,h,k):
    '''returns h and k, the coordinates to the vertex.

    '''
    standard_equation = 'y = a(x-h)^2 + k'
#    a = int(input('a = '))
#    b = int(input('b = '))
#    c = int(input('c = '))
#    y = int(input('y = '))
#    x = int(input('x = '))


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
    
    >>> pythagorean_theorem(3,4)  
    5.0
    
    >>> pythagorean_theorem(7,24) 
    25.0
    
    >>> pythagorean_theorem(361,42) 
    363.44
    '''
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
    '''
    rise = (y2-y1)
    run = (x2-x1)
    if run == 0:
        m = "undefined"
        print(m)
    else:
        m = (f"{rise} / {run}")
        print(m)
    
    
    
    
    
    
    

if __name__ == "__main__":
    import doctest
    doctest.testmod()


print()