from turtle import Turtle, Screen
import random


is_on = False
screen = Screen()
screen.setup(width = 400, height = 500)
user_bet = screen.textinput(title = 'Make your bet',prompt = 'Which turtle will win the race? Enter a color:')
y_position = [-70,-40,-10,20,50,80]
colors = ['red','black','yellow','orange','blue','purple']
all_turtles = []


for turtle_index in range(0,6):
    tim = Turtle(shape = 'turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-170,y = y_position[turtle_index] )
    all_turtles.append(tim)

if user_bet:
    is_on = True

while is_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won! The {winning_color} turtle is winning ')
            else:
                print(f'Youve lost! The {winning_color} turtle is winning ')
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()