"""Penta Spiral

This program already works. See if you can change it to make it draw a different pattern.

"""


import random
import turtle


# Returns a random color!
def getRandomColor():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


window = turtle.Screen()
window.bgcolor("white")

# Make a new turtle
diddy = turtle.Turtle()

# This code sets our shape to a turtle
diddy.shape("classic")

# Set your turtle's speed
diddy.speed(-10)

# Set your turtle's color
diddy.color("green")

# Use a loop to repeat the code below 50 times
for i in range(50):

    # Set the turtle color to a random color
    diddy.pencolor(getRandomColor())

    # Move the turtle (5*i) pixels. 'i' is the loop variable
    diddy.forward(9 * i)

    # Turn the turtle (360/7) degrees to the right
    diddy.right(360 / 7 + i*5)

    # Change the turtle width to 'i' (the loop variable)
    diddy.width(i)

    # Check the pattern against the picture in the recipe. If it matches, you are done!


turtle.done()

# Now check in your code!