'''
Hey there, feel free to implement your logic and also let me know how do you like it...
Also follow mi on Twitter:- @iamchaitanya99
'''

# Here we used turtle module to create window for our program
import turtle
import random

# Just a lis of no.s on Dice
list = [1, 2, 3, 4, 5, 6]

def diceroll():
    # A rnadom no. will be chosen
    r = random.choice(list)

    # Dots will be shown and hidden as per the given no. and condition
    if r == 1:
        done.showturtle()
        done.goto(0, 0)
        dtwo.hideturtle()
        dthree.hideturtle()
        dfour.hideturtle()
        dfive.hideturtle()
        dsix.hideturtle()
    elif r == 2:
        done.showturtle()
        done.goto(-30, 30)
        dtwo.showturtle()
        dtwo.goto(30, -30)
        dthree.hideturtle()
        dfour.hideturtle()
        dfive.hideturtle()
        dsix.hideturtle()
    elif r == 3:
        done.showturtle()
        done.goto(40, -40)
        dtwo.showturtle()
        dtwo.goto(0, 0)
        dthree.showturtle()
        dthree.goto(-40, 40)
        dfour.hideturtle()
        dfive.hideturtle()
        dsix.hideturtle()
    elif r == 4:
        done.showturtle()
        done.goto(40, 40)
        dtwo.showturtle()
        dtwo.goto(40, -40)
        dthree.showturtle()
        dthree.goto(-40, 40)
        dfour.showturtle()
        dfour.goto(-40, -40)
        dfive.hideturtle()
        dsix.hideturtle()
    elif r == 5:
        done.showturtle()
        done.goto(40, 40)
        dtwo.showturtle()
        dtwo.goto(40, -40)
        dthree.showturtle()
        dthree.goto(0, 0)
        dfour.showturtle()
        dfour.goto(-40, 40)
        dfive.showturtle()
        dfive.goto(-40, -40)
        dsix.hideturtle()
    else:
        done.showturtle()
        done.goto(-35, 50)
        dtwo.showturtle()
        dtwo.goto(-35, 0)
        dthree.showturtle()
        dthree.goto(-35, -50)
        dfour.showturtle()
        dfour.goto(35, 50)
        dfive.showturtle()
        dfive.goto(35, 0)
        dsix.showturtle()
        dsix.goto(35, -50)

# Window
wn = turtle.Screen()
wn.title("Dice by @DevDCtech")
wn.bgcolor('black')
wn.setup(width=500, height=500)
wn.tracer(0)

# Dice
dice = turtle.Turtle()
dice.speed(0)
dice.shape("square")
dice.shapesize(stretch_len=10, stretch_wid=10)
dice.pencolor("black")
dice.fillcolor("white")
dice.penup()

# Dice Dot One
done = turtle.Turtle()
done.hideturtle()
done.speed(0)
done.shape("circle")
done.shapesize(stretch_len=2, stretch_wid=2)
done.fillcolor("black")
done.penup()

# Dice Dot Two
dtwo = turtle.Turtle()
dtwo.hideturtle()
dtwo.speed(0)
dtwo.shape("circle")
dtwo.shapesize(stretch_len=2, stretch_wid=2)
dtwo.fillcolor("black")
dtwo.penup()

# Dice Dot Three
dthree = turtle.Turtle()
dthree.hideturtle()
dthree.speed(0)
dthree.shape("circle")
dthree.shapesize(stretch_len=2, stretch_wid=2)
dthree.fillcolor("black")
dthree.penup()

# Dice Dot Four
dfour = turtle.Turtle()
dfour.hideturtle()
dfour.speed(0)
dfour.shape("circle")
dfour.shapesize(stretch_len=2, stretch_wid=2)
dfour.fillcolor("black")
dfour.penup()

# Dice Dot Five
dfive = turtle.Turtle()
dfive.hideturtle()
dfive.speed(0)
dfive.shape("circle")
dfive.shapesize(stretch_len=2, stretch_wid=2)
dfive.fillcolor("black")
dfive.penup()

# Dice Dot Six
dsix = turtle.Turtle()
dsix.hideturtle()
dsix.speed(0)
dsix.shape("circle")
dsix.shapesize(stretch_len=2, stretch_wid=2)
dsix.fillcolor("black")
dsix.penup()

# Dice Roll
wn.onkeypress(diceroll, "r")
wn.listen()

# Main Loop
while True:
    wn.update()
