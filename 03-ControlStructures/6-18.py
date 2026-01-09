x = 5
y = 2

print(f"Point P({x},{y})", end=" ")

# Coordinates of the point
x = 5
y = 2

print(f"Point P({x},{y})", end=" ")

if x == 0 and y == 0:
    print("is at the origin (0,0) of the coordinate system")
elif x == 0:
    print("is on the y-axis")
elif y == 0:
    print("is on the x-axis")
elif x > 0 and y > 0:
    print("is in the first quadrant of the coordinate system")
elif x < 0 and y > 0:
    print("is in the second quadrant of the coordinate system")
elif x < 0 and y < 0:
    print("is in the third quadrant of the coordinate system")
elif x > 0 and y < 0:
    print("is in the fourth quadrant of the coordinate system")
