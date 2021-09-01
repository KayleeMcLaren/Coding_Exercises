
from turtle import Turtle, Screen

shelly = Turtle()
shelly.shape("turtle")
my_screen = Screen()


def move_forwards():
    shelly.forward(10)


def move_backwards():
    shelly.backward(10)


def turn_left():
    shelly.left(10)


def turn_right():
    shelly.right(10)


def clear():
    shelly.clear()
    shelly.penup()
    shelly.home()
    shelly.pendown()


my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="d", fun=turn_right)
my_screen.onkey(key="a", fun=turn_left)
my_screen.onkey(key="c", fun=clear)

my_screen.exitonclick()
