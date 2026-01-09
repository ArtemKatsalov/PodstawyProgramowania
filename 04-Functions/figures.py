###
# Draw a square
#
def draw_square(length):
    import turtle
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_triangle(length):
    import turtle
    for i in range(3):
        turtle.forward(length)
        turtle.right(120)

def draw_rectangle(length_a, length_b):
    import turtle
    for i in range(2):
        turtle.forward(length_a)
        turtle.right(90)
        turtle.forward(length_b)
        turtle.right(90)
