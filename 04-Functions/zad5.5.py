###
# Draws each of the figures (square, triangle, rectangle) twice,
# in different locations
#
import figures
import turtle

# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle
pen = turtle
pen.speed(5)

## Draw figures
figures.draw_square(50)
pen.penup()
pen.goto(-100, 100)
pen.pendown()
figures.draw_square(50)

pen.penup()
pen.goto(100, 100)
pen.pendown()
figures.draw_triangle(50)
pen.penup()
pen.goto(100, -100)
pen.pendown()
figures.draw_triangle(50)

pen.penup()
pen.goto(-100, -100)
pen.pendown()
figures.draw_rectangle(60, 30)
pen.penup()
pen.goto(0, 100)
pen.pendown()
figures.draw_rectangle(60, 30)

pen.hideturtle()
window.mainloop()
