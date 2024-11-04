Num=int(input("Please enter a number: "))
print("Following is your Number: ", Num)

if (Num == 1):
    print("The Number you have entered is 1")
    
elif (Num > 0):
    if (Num > 10):
        print("Number is Greater than  10")
    elif (Num >= 1 and Num <= 10):
        print("Number is between 1 to 10")
else:
    print("Number is less than 0")
        