import math 
    
def vertex_form():
    '''returns h and k, the coordinates to the vertex.

    '''
    standard_equation = 'y = a(x-h)^2 + k'
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    y = int(input('y = '))
    x = int(input('x = '))
    
    print(a)

#x1 = int(input('x1 = '))
#y1 = int(input('y1 = '))
#x2 = int(input('x2 = '))
#y2 = int(input('y2 = '))

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
    
if __name__ == "__main__":
    #dist_formula(1,1,1,2)
    import doctest
    doctest.testmod()


print()