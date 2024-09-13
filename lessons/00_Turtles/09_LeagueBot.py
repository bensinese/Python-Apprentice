""" Leaguebot

Write your own turtle program! Here is what your program should do

1) Change the turtle image to 'leaguebot_bolt.gif'
2) Change the turtle size to 10x10
3) Change the turtle line color to 'blue'
4) Draw a hexagon using a loop and variables. 

"""

import turtle as turtle

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

tina = turtle.Turtle()
tina.shape('turtle')  
... # Your Code here

tina.color("green")
tina.penup()
tina.speed(3)

tina.turtlesize(stretch_wid=10, stretch_len=10, outline=4)

turtle.exitonclick()     

