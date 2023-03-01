#Emily Nixon

import turtle
mood=input("What is your mood (happy,sad,sleepy,angry)?\n")
riley=turtle.Turtle()
riley.width(5)
riley.speed(2)
def draw_mood_star(mood):
    if mood == "happy":
        riley.color("green")
    elif mood == "sad":
        riley.color("blue")
    elif mood == "sleepy":
        riley.color("purple")
    else:
        riley.color("red")
    for side in range(5):
        riley.forward(100)
        riley.right(144)
draw_mood_star(mood)
