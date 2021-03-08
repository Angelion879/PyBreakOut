import turtle
from walls import wall_builder
from walls import coord
from walls import Brick

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
        #self.dx = 1
        self.dy = 0.5

paddle = Paddle((0, -300))
ball = Ball((0,-279))

# Functions

def paddle_right():
    x = paddle.xcor()
    x+= 20
    paddle.setx(x)

def paddle_left():
    x = paddle.xcor()
    x-=20
    paddle.setx(x)


# Key binding
win.listen()
win.onkeypress(paddle_right, 'Right')
win.onkeypress(paddle_left, 'Left')

# Wall Building 
wall_builder()
win.update()

while True:
    win.update()

    # Ball movement
    #ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Colision
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.ycor() < -340:
        paddle.goto(0, -300)
        ball.goto(0,-279)
        ball.dy *= -1

    # Paddle colision
    if (ball.ycor() < -280 and ball.ycor() > -290) and (ball.xcor() < (paddle.xcor() +50) and ball.xcor() > (paddle.xcor() - 50)):
        ball.sety(-280)
        ball.dy *= -1

    # Bricks colision
    if ((ball.xcor()), (ball.ycor() +10)) in coord:
        print("YUP, IT IS HERE")
        brick = Brick(((ball.xcor()), (ball.ycor() +10)), 'black')
        coord.remove(((ball.xcor()), (ball.ycor() +10)))
        ball.dy *= -1