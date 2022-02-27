import os
import sys
import turtle
import game

# define audio and image resource location for packaging as standalone .exe
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

filename = os.path.basename((__file__))

#create game window
window = turtle.Screen()
window.cv._rootwindow.resizable(False, False)
window.title("Vocablemy")
window.bgcolor("#232323")
window.setup(width=600, height=400)
window.tracer(0)

word = turtle.Turtle()
word.speed(0)
word.shape("square")
word.color("white")
word.penup()
word.hideturtle()
word.goto(0,170)
word.write("", align="center", font=("", 12, "normal"))

#intro/tutorial screen
while game.started == 0:
    window.update()

#after game start
while game.started == 1:
    window.update()