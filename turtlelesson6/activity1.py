import turtle

# creating canvas
turtle.Screen().bgcolor("blue")
#length and width of the screen

sc = turtle.Screen()
sc.setup(1000, 700)

turtle.title("Welcome to Turtle Window")

# turtle object creation
board = turtle.Turtle()

# creating a rectangle
for i in range(4):
	board.forward(250)
	board.left(90)
	i = i+1