import turtle

class Brick(turtle.Turtle):
    def __init__(self,position,color):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed(0)
        self.penup()
        self.color(color)
        self.goto(position)

brick = Brick((-340, 360), 'white')

wall_type = [brick]