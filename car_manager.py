from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(270)
        self.shapesize(2, 1)
        self.goto(300, random.randint(-240, 250))
        self.color(random.choice(COLORS))
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.ycor())
