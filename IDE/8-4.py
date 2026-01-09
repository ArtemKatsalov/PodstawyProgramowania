#
# A program that prints your height both in cm and in feet and inches.
#

cm = 170

# convert cm to total inches
total_inches = cm / 2.54

# calculate the number of feet
feet = int(total_inches // 12)

# calculate remaining inches
inches = int(total_inches % 12)

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
