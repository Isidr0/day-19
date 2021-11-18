from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# tim.goto(x=-230, y=150)
x = -230
y = 100
turtle_list = []

for color in colors:
    print(color)
    color_turtle = Turtle(shape="turtle")
    color_turtle.color(color)
    color_turtle.penup()
    y -= 30
    color_turtle.sety(y)
    color_turtle.setx(x)
    print(color_turtle)
    turtle_list.append(color_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



# for turtle in turtle_list:
#     turtle_list.forward(10)
#     # while turtle.xcor() < 200:
#
# random_amount = random.randint(1, 10)
#
# for i in range(len(turtle_list)):
#     print(i)
#     turtle_list[i].forward(random_amount)




# Functions as inputs

# Higher order functions are functions that can work with other functions.
# Apparently this isn't possible in some programming languages.

# When using methods that aren't your own it's recommended to use keyword arguments over positional arguments.
# Since you won't know what they mean on their own.

# don't add parens when using a function as an argument.
# the parens trigger the function to happen immediately. but we want to trigger the function to happen on a key press.
# screen.onkey(key="space", fun=move_forwards)

# Create etch a sketch with wasd as movement keys.
# Should be able to press both at once to move diagonally. Press c to clear.
# w = forward s = backward a = counter-clockwise d = clockwise


#allows scren to detect keyboard input
# screen.listen()
#
# def move_forward():
#     tim.forward(10)
#
# def move_left():
#     # tim.left(10)
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def move_back():
#     tim.back(100)
#
# def move_right():
#     # tim.right(10)
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear_screen():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.onkeypress(key="w", fun=move_forward)
# screen.onkeypress(key="a", fun=move_left)
# screen.onkeypress(key="s", fun=move_back)
# screen.onkeypress(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()


