import turtle

class Brick(turtle.Turtle):
    def __init__(self,position):
        super().__init__(shape='square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.speed(0)
        self.penup()
        self.color('white')
        self.goto(position)

coord = []

def wall_builder():
    global coord
    for y in range(340, 30, -30):
        for x in range(-360, 390, 65):
            brick = Brick((x, y))
            if (x,y) not in coord:
                coord.append((x,y))
