from turtle import Turtle

STARTING_SEGMENTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_FORWARD = 20
TURN_UP = 90
TURN_DOWN = 270
TURN_RIGHT = 0
TURN_LEFT = 180


class Snake():
    def __init__(self):
        self.seg = []
        self.Create_snake()
        self.Head = self.seg[0]

    def Create_snake(self):
        for position in STARTING_SEGMENTS:
            self.add_segment(position)

    def add_segment(self, position):
        New_Seg = Turtle("square")
        New_Seg.penup()
        New_Seg.color("green")
        New_Seg.goto(position)
        self.seg.append(New_Seg)

    def extend(self):
        self.add_segment(self.seg[-1].position())

    def move(self):
        for s_seg in range(len(self.seg) - 1, 0, -1):
            x_pos = self.seg[s_seg - 1].xcor()
            y_pos = self.seg[s_seg - 1].ycor()
            self.seg[s_seg].goto(x_pos, y_pos)
        self.seg[0].forward(MOVE_FORWARD)

    def Up(self):
        if self.Head.heading() != TURN_DOWN:
            self.Head.setheading(TURN_UP)

    def Down(self):
        if self.Head.heading() != TURN_UP:
            self.Head.setheading(TURN_DOWN)

    def Right(self):
        if self.Head.heading() != TURN_LEFT:
            self.Head.setheading(TURN_RIGHT)

    def Left(self):
        if self.Head.heading() != TURN_RIGHT:
            self.Head.setheading(TURN_LEFT)

