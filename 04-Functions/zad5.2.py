import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'100cm = {converters.cm_to_inches(100):.2f} inches')
print(f'5 feet 8 inches = {converters.feet_and_inches_to_cm(5, 8):.2f} cm')
