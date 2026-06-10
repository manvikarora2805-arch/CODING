import turtle

# 1. Setup the screen and background color
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Sets the background to light blue

# 2. Create the turtle and set its style
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.pensize(5)  # Makes the drawing lines thicker

# ==========================================
# DRAWING 1: EQUILATERAL TRIANGLE (3 sides)
# ==========================================
my_turtle.penup()
my_turtle.goto(-200, 0)  # Move turtle to the left side
my_turtle.pendown()

my_turtle.color("red", "yellow")  # Red border, yellow fill
my_turtle.begin_fill()

# Side 1
my_turtle.forward(100)
my_turtle.left(120)
# Side 2
my_turtle.forward(100)
my_turtle.left(120)
# Side 3
my_turtle.forward(100)
my_turtle.left(120)

my_turtle.end_fill()

# ==========================================
# DRAWING 2: RECTANGLE (4 sides)
# ==========================================
my_turtle.penup()
my_turtle.goto(-20, 0)  # Move turtle to the middle
my_turtle.pendown()

my_turtle.color("blue", "pink")  # Blue border, pink fill
my_turtle.begin_fill()

# Draw the sides
my_turtle.forward(150)  # Long side
my_turtle.left(90)
my_turtle.forward(80)  # Short side
my_turtle.left(90)
my_turtle.forward(150)  # Long side
my_turtle.left(90)
my_turtle.forward(80)  # Short side
my_turtle.left(90)

my_turtle.end_fill()

# ==========================================
# DRAWING 3: HEXAGON (6 sides)
# ==========================================
my_turtle.penup()
my_turtle.goto(180, 0)  # Move turtle to the right side
my_turtle.pendown()

my_turtle.color("purple", "orange")  # Purple border, orange fill
my_turtle.begin_fill()

# Repeat forward and turn 6 times
for _ in range(6):
    my_turtle.forward(60)
    my_turtle.left(60)  # 360 divided by 6 sides = 60 degrees

my_turtle.end_fill()