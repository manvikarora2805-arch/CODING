import turtle

# Create a turtle object
t = turtle.Turtle()

# Set drawing speed (1-10)
t.speed(3)

# Draw an equilateral triangle
for i in range(3):
    t.forward(100)  # Move forward 100 units
    t.left(120)     # Turn left 120 degrees

# Keep the window open
turtle.done()