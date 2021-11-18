from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()



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
screen.listen()

def move_forward():
    tim.forward(10)

def move_left():
    # tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_back():
    tim.back(100)

def move_right():
    # tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="s", fun=move_back)
screen.onkeypress(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)


screen.exitonclick()


