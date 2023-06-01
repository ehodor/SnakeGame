# Emma Hodor

from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,330)
        self.write(f"Score: {self.score}",align='center',font=('Comic Sans', 16, 'normal'))

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align='center',font=('Comic Sans', 16, 'normal'))

    def joever(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game over! Your score is {self.score}.", align="center", \
        font=('Comic Sans', 16, 'normal'))