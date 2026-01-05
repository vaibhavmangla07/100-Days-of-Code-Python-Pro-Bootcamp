import random
import turtle

t = turtle.Turtle()
screen = turtle.Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
direction = [0, 90, 180, 270]
t.pensize(10)
t.speed("fast")

for _ in range(250):
    t.color(random.choice(colours))
    t.forward(30)
    t.setheading(random.choice(direction))

screen.exitonclick()