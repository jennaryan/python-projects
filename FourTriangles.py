import turtle
import random
bob = turtle.Turtle()
b = bob
def colour_random():
    r = random.random()
    g = random.random()
    b = random.random()
    return(r,g,b)


for count in range(0,4):
    b.forward(100)
    b.right(90)


b.right(60)
b.forward(100)
b.left(120)
b.forward(100)


