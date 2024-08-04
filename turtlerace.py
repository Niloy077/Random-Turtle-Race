from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

def draw_box_with_message(message, x, y):
    # Draw the box
    turtle = Turtle()
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.write(message, align="center", font=("Arial", 16, "normal"))

# Setup for the turtle race
user_bet = screen.textinput(title="Make Your bet", prompt="Which turtle will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 200:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                s = "You've won! The " + winning_color + " turtle is the winner!"
                draw_box_with_message(s, 0, 0)
            else:
                s = "You've lost! The " + winning_color + " turtle is the winner!"
                draw_box_with_message(s, 0, 0)
        
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
