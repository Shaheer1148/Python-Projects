import time

timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timehour =int(time.strftime("%H"))
print(timehour)
timemin = int(time.strftime("%M"))
print(timemin)
timesec = int(time.strftime("%S"))
print(timesec)

if timehour >= 25:
    print("the time is invalid")
elif timehour >= 0 and timehour <= 4:
    print("What the fuck Sir go to Sleep")
elif timehour >= 5 and timehour <= 10:
    print("Good Morning Sir")
elif timehour >= 11 and timehour <= 16:
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")