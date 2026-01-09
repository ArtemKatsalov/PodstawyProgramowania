###
#checks what number was entered from the keyboard and
#prints one of the messages below

number = int(input('Enter the number: '))
if number > 0:
    print('Number is positive')
elif number < 0:
     print('Number is negative')
else:
     print('Number is 0')