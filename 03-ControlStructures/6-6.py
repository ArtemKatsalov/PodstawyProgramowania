parking_hours = int(input("Enter number of hours of parking: "))

if parking_hours > 0 and parking_hours < 3:
    print("The parking fee is: 5PLN")
elif parking_hours >= 3 and parking_hours <= 6:
    print("The parking fee is: 15PLN")
elif parking_hours > 6:
    print("The parking fee is: 20PLN")
else:
    print("The parking fee is: 0PLN")