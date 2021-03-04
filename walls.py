import turtle

class Brick(turtle.Turtle):
    def __init__(self,position):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.speed(0)
        self.penup()
        self.color('white')
        self.goto(position)

#brick = Brick((-360, 340))

for i in range(-360, 390, 65):
    brick = Brick((i, 340))
