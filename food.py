import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        food_x = random.randint(-270, 270)
        food_y = random.randint(-270, 270)

        if food_x % 10 != 0 and food_y % 10 !=0:
            self.refresh()
        else:
            self.goto(food_x, food_y)