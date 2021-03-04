import turtle
import walls

win = turtle.Screen()
win.title("BreakOut by @Angelion879")
win.bgcolor("black")
win.setup(width=800, height=700)
win.tracer(0)

class Paddle(turtle.Turtle):
    def __init__(self,position):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed(0)
        self.penup()
        self.color('white')
        self.goto(position)
class Ball(turtle.Turtle):
    def __init__(self,position):
        super().__init__(shape='circle')
        self.speed(0)
        self.penup()
        self.color('white')
        self.goto(position)

paddle = Paddle((0, -300))
ball = Ball((0,-279))

while True:
    win.update()