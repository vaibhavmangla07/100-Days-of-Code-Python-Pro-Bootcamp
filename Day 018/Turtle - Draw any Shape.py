import turtle

t = turtle.Turtle()
screen = turtle.Screen()

def draw_shape(shape):
    angle = 360/shape
    for _ in range(shape):
        t.forward(70)
        t.right(angle)

for i in range(3, 11):
    draw_shape(i)
screen.exitonclick()
