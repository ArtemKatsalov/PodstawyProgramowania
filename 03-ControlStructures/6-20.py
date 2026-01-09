dec = int(input("Enter a decimal number: "))
bin = " "
while dec > 0:
    remainder = dec % 2
    bin = str(remainder) + bin
    dec = dec // 2
print(bin)  