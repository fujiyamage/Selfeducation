import turtle
turtle.showturtle()
turtle.speed(1)

TOP_X = 0
TOP_Y = 100
LEFT_X = -100
LEFT_Y = - 100
RIGHT_X = 100
RIGHT_Y = -100

def main():
    first_action()
    line(RIGHT_X, RIGHT_Y, "red")
    line(LEFT_X, LEFT_Y, "blue")
    line(TOP_X, TOP_Y, "green")
    turtle.done()

def line(x, y, color):
    turtle.color(color)
    turtle.pendown()
    turtle.goto(x, y)

def first_action():
    turtle.penup()
    turtle.goto(TOP_X, TOP_Y)

main()