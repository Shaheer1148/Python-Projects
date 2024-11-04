def average (*number):
    sum = 0
    for i in number:
        sum = sum + i
    return sum / len(number)

c = average (5,5,2,1)
print("The average is", c)

