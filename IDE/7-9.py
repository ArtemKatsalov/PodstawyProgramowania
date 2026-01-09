import random

dice_roll = random.randint(1,6)
special = dice_roll == 1 or dice_roll == 6
print(f'dice_roll: {dice_roll}, this number is special(1 or 6):{special}')