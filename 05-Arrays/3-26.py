import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values (degrees)
for angle in range(0, 361):
    x.append(angle)

# create y values (sin of angle)
for angle in x:
    y.append(math.sin(math.radians(angle)))

# draw the chart
plt.plot(x, y)
plt.xlabel("Angle (degrees)")
plt.ylabel("sin(x)")
plt.title("y = sin(x)")
plt.show()
