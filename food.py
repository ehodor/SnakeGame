# Emma Hodor

from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.penup()
        self.speed("fastest")
        self.color("brown")
        rand_x = random.randint(-330,330)
        rand_y = random.randint(-330,330)
        self.goto(rand_x, rand_y)

    def move(self):
        rand_x = random.randint(-330, 330)
        rand_y = random.randint(-330, 330)
        self.goto(rand_x, rand_y)
