# Emma Hodor

from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("green")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
cur_score = Score()
game = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while game:
    screen.update()
    time.sleep(.07)
    snake.move()
    if snake.all_turtle[0].distance(food) < 20:
        food.move()
        cur_score.increment()
        snake.add_segment()
    if snake.all_turtle[0].xcor() > 350 or snake.all_turtle[0].xcor() < -350\
    or snake.all_turtle[0].ycor() > 350 or snake.all_turtle[0].ycor() < -350:
        game = False
    for i in range(len(snake.all_turtle)-2):
        if snake.all_turtle[0].distance(snake.all_turtle[i+1]) < 10:
            game = False

cur_score.joever()
screen.exitonclick()
