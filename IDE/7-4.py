circumference = int(input('Enter tree circumference in cm: '))
diameter = circumference / 3.14
can_cut = diameter >= 50
print(f'Tree can be cut down: {can_cut}  ')