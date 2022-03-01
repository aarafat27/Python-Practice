from turtle import *
import turtle

state = {'turn': 0}
screen = turtle.Screen()
screen.bgcolor('#0a425b')

speed = int(input('Enter the speed :'))


def spin():
    clear()
    angle = state['turn'] / 5
    right(angle)
    forward(100)
    dot(120, 'red')
    back(100)
    right(120)
    forward(100)
    dot(120, 'blue')
    back(100)
    right(120)
    forward(100)
    dot(120, 'green')
    back(100)
    right(120)
    update()


def animate():
    if state['turn'] > 0:
        state['turn'] -= 1
    spin()
    ontimer(animate, 20)


def flick():
    state['turn'] += speed


hideturtle()
tracer(False)
onkey(flick, 'space')
listen()
animate()
done()
