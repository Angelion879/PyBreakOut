import turtle

class Brick(turtle.Turtle):
    def __init__(self,position,color):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(position)

brick = Brick((-375, 340), 'white')
brick2 = Brick((-310, 340), 'white')