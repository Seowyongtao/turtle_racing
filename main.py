from turtle import Turtle, Screen
from random import randint


myScreen = Screen()
myScreen.setup(width=500, height=400)
user_bet = myScreen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Pick a color: ")
colors = ["red", "green", "blue", "yellow", "black", "orange"]
all_turtles = []
is_bet = False

y_position = -60

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-225, y=y_position)
    y_position += 30
    all_turtles.append(new_turtle)

if user_bet:
    is_bet = True

while is_bet:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_bet = False

            if user_bet == turtle.pencolor():
                print(f"You've won ! {turtle.pencolor()} turtle is the winner !")
            else:
                print(f"You've lose ! {turtle.pencolor()} turtle is the winner !")

        turtle.forward(randint(0, 10))


myScreen.exitonclick()
