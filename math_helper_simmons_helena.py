import math 

def vertex_form():
    '''
    returns h and k, the coordinates to the vertex.
    '''
    standard_equation = 'y = a(x-h)^2 + k'
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    x = int(input('x = '))
    print(a)
    
def distance formula():
    '''
    returns the distance between two sets of coordinates
    '''
    x1 = int(input('x1 = '))
    y1 = int(input('y1 = '))
    x2 = int(input('x2 = '))
    y2 = int(input('y2 = '))
    
    dist = math.sqrt((x1-x2)) #VERY MUCH INCOMPLETE
    
    
if __name__ == "main":
    import doctest
    doctest.testmod()
print()