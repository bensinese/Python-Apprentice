"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""



# Double click on this cell to copy the code

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = turtle.Turtle()
t.penup()
t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

def turtle_clicked(t, x, y):

    print('turtle clicked!')
    
    for i in range(0,360, 20):
        t.tilt(20)

t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))

turtle.done() # Important! Use `done` not `exitonclick` to keep the window open
