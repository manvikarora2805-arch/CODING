







import turtle
 
t = turtle.Turtle()

l = int(input("Enter the length:"))
w = int(input("Enter the width:"))

# drawing first side
t.forward(l) 
t.left(90) 

# drawing second side
t.forward(w) 
t.left(90) 

# drawing third side
t.forward(l) 
t.left(90) 

# drawing fourth side
t.forward(w) 
t.left(90)








# import the turtle modules
import turtle

# Start a work Screen
ws = turtle.Screen()

# Define a Turtle Instance
geekyTurtle = turtle.Turtle()

# executing loop 6 times for 6 sides
for i in range(6):

    # Move forward by 90 units
    geekyTurtle.forward(90)

    # Turn left the turtle by 300 degrees
    geekyTurtle.left(300)