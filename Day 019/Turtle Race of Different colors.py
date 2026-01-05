import random
from turtle import Turtle, Screen

is_race = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Choose the color: ")
colors = ["red", "yellow", "blue", "green", "purple", "black"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(0, 6):
    new_t = Turtle(shape="turtle")
    new_t.color(colors[i])
    new_t.penup()
    new_t.goto(x=-230, y=y_pos[i])
    all_turtles.append(new_t)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet.lower():
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
            break
        turtle.forward(random.randint(0, 10))

screen.exitonclick()