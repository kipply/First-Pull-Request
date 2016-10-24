#imports and name program. This is a gr8 program that will draw triangles inside triangles inside triangles inside triangles...
import turtle
import random
import re
import sys #to take command line arguments
import logging #to tell your console stuff that you did wrong or right
PROGNAME = 'Sierpinski'

#make turtle, draw in white and control speed
pen = turtle.Turtle()
pen.speed(4)
pen.pencolor("white")

#hide the turtle
turtle.hideturtle()
pen.ht()

#manage screen, random background
screen = turtle.getscreen()
screen.colormode(255)
r = random.randrange(0, 257, 10)
g = random.randrange(0, 257, 10)
b = random.randrange(0, 257, 10)
screen.bgcolor(r, g, b)

#TODO: Make it expand to screen size. Hopefully python will make it easy for me. 
points = [[-280,-200],[0,280],[280,-200]] #plots points. 1.4x between the numbers

#I'm trying to practice commenting but this function is real straightforward.
def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) 

def triangle(points,depth):

    pen.up()
    pen.goto(points[0][0],points[0][1])
    pen.down()
    pen.goto(points[1][0],points[1][1])
    pen.goto(points[2][0],points[2][1])
    pen.goto(points[0][0],points[0][1])

    if depth>0:
        triangle([points[0],
            getMid(points[0], points[1]),
            getMid(points[0], points[2])], depth-1)
        triangle([
            points[1],
            getMid(points[0], 
            points[1]),
            getMid(points[1], 
            points[2])]
        ,depth-1)
        triangle([points[2],
            getMid(points[2], 
            points[1]),
            getMid(points[0], 
            points[2])],
        depth-1)


triangle(points,6)
