import turtle
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.start()
        self.head = self.segments[0]

    def add_segment(self, x, y):
        new_segment = turtle.Turtle()
        new_segment.penup()
        new_segment.shape('square')
        new_segment.color("white", "white")
        new_segment.goto(x, y)
        self.segments.append(new_segment)

    def start(self):
        for i in range(3):
            self.add_segment(x=-20 * i, y=0)

    def turn_left(self):
        if self.head.heading() == 0:
            return
        else:
            self.head.setheading(180)

    def turn_right(self):
        if self.head.heading() == 180:
            return
        else:
            self.head.setheading(0)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.start()
        self.head = self.segments[0]

    def turn_up(self):
        if self.head.heading() == 270:
            return
        else:
            self.head.setheading(90)

    def turn_down(self):
        if self.head.heading() == 90:
            return
        else:
            self.head.setheading(270)

    def move(self):
        # for segment in self.segments[::-1]:
        for segment in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[segment-1].xcor()
            new_y = self.segments[segment-1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def grow(self):
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        self.add_segment(x=x, y=y)