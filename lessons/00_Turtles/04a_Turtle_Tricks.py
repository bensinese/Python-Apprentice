"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.
"""



# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.penup()
tina.goto(60,-20)

tina.pendown()
tina.color("black")
tina.begin_fill()
tina.circle(90)
tina.end_fill()



tina.goto(40,155)
tina.left(180)
tina.color("red")
tina.begin_fill()
tina.circle(90,180)
tina.end_fill()

tina.penup()
tina.goto(80,-25)
tina.left(360)
tina.color("red")
tina.begin_fill()
tina.circle(90,180)
tina.end_fill()

tina.goto(90,155)
tina.color("black")
tina.right(90)
tina.begin_fill()
tina.circle(30,180)
tina.end_fill()

turtle.exitonclick()