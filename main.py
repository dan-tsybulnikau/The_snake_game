import turtle as t
import time
import snake
import food
import score

my_screen = t.Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor('black')
my_screen.title('The Snake Game')
my_screen.tracer(0)
game_is_on = True

my_snake = snake.Snake()
my_score = score.Score()
food = food.Food()

my_screen.listen()
my_screen.onkeypress(key='Left', fun=my_snake.turn_left)
my_screen.onkeypress(key='Right', fun=my_snake.turn_right)
my_screen.onkeypress(key='Up', fun=my_snake.turn_up)
my_screen.onkeypress(key='Down', fun=my_snake.turn_down)

while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    my_snake.move()

    if my_snake.head.distance(food) < 15:
        food.refresh()
        for seg in my_snake.segments:
            if food.xcor() - seg.xcor() < 20 or food.ycor() - seg.ycor() < 20:
                food.refresh()
        my_score.inc_score()
        my_snake.grow()

    if my_snake.head.xcor() > 298 \
            or my_snake.head.ycor() > 300\
            or my_snake.head.xcor() < -300\
            or my_snake.head.ycor() < -298:
        my_score.reset()
        my_snake.reset()

    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 2:
            my_score.reset()
            my_snake.reset()
if my_screen.bye():
    my_score.reset()
my_screen.exitonclick()