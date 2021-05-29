import turtle
ALIGNMENT = 'center'
FONT = ("Courier", 14, "bold")


class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as text:
            self.high_score = int(text.read())
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def inc_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as text:
                text.write(str(self.high_score))
        self.score = 0
        self.write_score()
