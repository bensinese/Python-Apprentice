"""

Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. The access those
lists to draw the pattern.

hint: all of your lists should have the same number of elements.
Review the ' Using Lists' section of the previous lesson if you need 
more help

"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(10)                           # Make the turtle move as fast, but not too fast. 


forwards = [ 27, 35, 46, 14, 67,26, 67, 23, 43, 98 ]
lefts = [ 26, 67, 23, 43, 98, 45, 27, 35, 46, 14, 67]
colors = ['green', 'blue','red','yellow','orange','pink','blue','red','yellow','orange','pink']


for i in range(10):

    forward = [27, 27, 35, 46, 14, 67, 26, 67, 23, 43, 98]
    left = [26, 67, 23, 43, 98, 45, 27, 35, 46, 14, 67]
    color = ['green', 'blue','red','yellow','orange','pink','blue','red','yellow','orange','pink']


    tina.color(colors[i])
    tina.forward(forwards[i])
    tina.left(lefts[i])

turtle.exitonclick()  

