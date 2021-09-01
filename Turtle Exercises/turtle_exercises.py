
import turtle
from turtle import Turtle, Screen
import random

shelly = Turtle()
shelly.shape("turtle")
shelly.color("SkyBlue1")

# Exercise 1 - Draw a Square
for _ in range(4):
  shelly.forward(100)
   shelly.left(90)

    
# Exercise 2 - Draw a Dashed Line
for _ in range(15):
   shelly.forward(10)
   shelly.penup()
   shelly.forward(10)
   shelly.pendown()

  
# Exercise 3 - Draw a random shape
colours = ["DarkMagenta", "DeepSkyBlue", "LawnGreen", "HotPink", "LightSlateBlue", "OrangeRed", "yellow", "violet", "purple4", "DarkOrange"]

def draw_shape(num_sides):
  angle = 360 / num_sides
  for _ in range(num_sides):
    shelly.forward(100)
    shelly.right(angle)

    
 for shape_side_n in range(3, 11):
  shelly.color(random.choice(colours))
  draw_shape(shape_side_n)


# Exercise 4 - Draw a random walk
turtle.colormode(255)

def random_colour():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_colour = (r, g, b)
  return random_colour


directions = [0, 90, 180, 270]

shelly.speed(10)
shelly.pensize(5)

for i in range(100):
  shelly.color(random_colour())
  shelly.forward(30)
  shelly.setheading(random.choice(directions))


# Exercise 5 - Draw a spirograph
turtle.colormode(255)

shelly.speed(11)
shelly.pensize(2.5)

def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour


for _ in range(36):
    shelly.color(random_colour())
    shelly.circle(80)
    current_heading = shelly.heading()
    shelly.setheading(current_heading + 10)

my_screen = Screen()
my_screen.exitonclick()
