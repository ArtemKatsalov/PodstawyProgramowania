age = int(input("Enter your age: "))

if 0 < age < 13:
    print("Your age group is : Child")
elif 0 < age < 20:
    print("Your age group is : Teen")
elif 0 < age < 65:
    print("Your age group is : Adult")
elif 0 < age > 64:
    print("Your age group is : Senior")
else:
    print("Wrong age")