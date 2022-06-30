import turtle as t
import random
tim= t.Turtle()
t.colormode(255)


def random_c():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)
for i in range(100):
    tim.speed("fastest")
    tim.color(random_c())
    tim.circle(80)
    tim.left(55)

screen = t.Screen()
screen.exitonclick()
