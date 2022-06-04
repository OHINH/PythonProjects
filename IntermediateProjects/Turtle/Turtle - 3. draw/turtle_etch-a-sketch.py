from turtle import Turtle, Screen, back, left

Tim = Turtle()
screen = Screen()

def forward():
    Tim.forward(10)

def backward():
    Tim.backward(10)

def turn_left():
    Tim.left(10)

def turn_right():
    Tim.right(10)

def clear():
    Tim.home()
    Tim.clear()

screen.listen()
screen.onkeypress(fun=forward,key='o')
screen.onkeypress(fun=backward,key='l')
screen.onkeypress(fun=turn_left,key='k')
screen.onkeypress(fun=turn_right,key='m')
screen.onkeypress(fun=clear,key='c')

screen.exitonclick()