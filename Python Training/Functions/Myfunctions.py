# if we want to use a particular part of code 
# multiple times then we use functions

def Calculatemean (a , b):
    mean = (a + b)/2
    print(mean)


Calculatemean (3, 2)
Calculatemean (-1, 5)

def emptyfuction (g, h):
    pass #will write this function later


def isgreater (c, d):
    if c > d:
        print('c is greater than d')
    elif c == d:
        print('c and d are equal')
    else:
        print('d is greater than c')

isgreater (3, 5)
isgreater (6, 6)
isgreater (5, 1)