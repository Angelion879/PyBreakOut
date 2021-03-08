import turtle

class Brick(turtle.Turtle):
    def __init__(self,position, col):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.speed(0)
        self.penup()
        self.color(col)
        self.goto(position)

coord = []

def wall_builder():
    global coord
    brick = Brick((0,0), 'white')
    brick = Brick((0, 30), 'white')
    coord.append((0,0))
    coord.append((0,30))