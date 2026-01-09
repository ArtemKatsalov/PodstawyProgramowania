import turtle
import figures

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle
pen.speed(5)

# Side length
side_length = 100

# Draw a square
figures.draw_square(side_length)

# Hide the turtle and finish
pen.hideturtle()
window.mainloop()
