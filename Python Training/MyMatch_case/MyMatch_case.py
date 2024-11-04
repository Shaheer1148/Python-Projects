# Notes:

# Underscore is used for default

# in C++ and C break is necessary so that a
# particular case runs other was the other cases
# will also run if break is not used

# you can create 4 default cases

x = int(input("Enter your value: "))

match x:
    case 0:
        print ("x is zero")
        
    case 4:
        print("case is 4")
    
    case _: #this is the default case
        print(x)