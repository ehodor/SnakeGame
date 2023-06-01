# Emma Hodor

from turtle import Turtle


class Snake:
    def __init__(self):
        self.all_turtle = []
        self.start_coords = 0
        for i in range(5):
            new_turt = Turtle(shape="square")
            new_turt.color("aqua")
            new_turt.penup()
            new_turt.setpos(self.start_coords, 0)
            self.all_turtle.append(new_turt)
            self.start_coords -= 20

    def add_segment(self):
        new_turt = Turtle(shape="square")
        new_turt.color("aqua")
        new_turt.penup()
        vec = self.all_turtle[-1].position()
        new_turt.setpos(vec)
        self.all_turtle.append(new_turt)

    def up(self):
        self.move()
        if self.all_turtle[0].heading() != 270:
            self.all_turtle[0].setheading(90)
        #self.all_turtle[0].forward(20)

    def left(self):
        self.move()
        if self.all_turtle[0].heading() != 0:
            self.all_turtle[0].setheading(180)
        #self.all_turtle[0].forward(20)

    def right(self):
        self.move()
        if self.all_turtle[0].heading() != 180:
            self.all_turtle[0].setheading(0)
        #self.all_turtle[0].forward(20)

    def down(self):
        self.move()
        if self.all_turtle[0].heading() != 90:
            self.all_turtle[0].setheading(270)
        #self.all_turtle[0].forward(20)
    def move(self):
        for index in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[index-1].xcor()
            new_y = self.all_turtle[index-1]. ycor()
            self.all_turtle[index].goto(x=new_x, y=new_y)
        self.all_turtle[0].forward(20)

