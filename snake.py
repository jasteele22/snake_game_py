from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segment_index = []
        self.create_snake()
        self.head = self.segment_index[0]
        self.heading = self.head.heading()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("slowest")
        new_segment.setposition(position)
        self.segment_index.append(new_segment)

    def reset_snake(self):
        for seg in self.segment_index:
            seg.goto(-1000, -1000)
        self.segment_index.clear()
        self.create_snake()
        self.head = self.segment_index[0]

    def extend(self):
        self.add_segment(self.segment_index[-1].position())

    def move(self):
        for seg_num in range(len(self.segment_index) - 1, 0, -1):
            new_x = self.segment_index[seg_num - 1].xcor()
            new_y = self.segment_index[seg_num - 1].ycor()
            self.segment_index[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.heading = self.head.heading()

    def up(self,):
        if self.heading != 270:
            self.head.setheading(90)
        else:
            self.head.setheading(270)

    def down(self,):
        if self.heading != 90:
            self.head.setheading(270)
        else:
            self.head.setheading(90)

    def left(self):
        if self.heading != 0:
            self.head.setheading(180)
        else:
            self.head.setheading(0)

    def right(self):
        if self.heading != 180:
            self.head.setheading(0)
        else:
            self.head.setheading(180)
