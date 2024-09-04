import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = []
car = CarManager()
cars.append(car)

screen.listen()
screen.onkey(player.move, "Up")

loop_counter = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_counter += 1
    if loop_counter == 6:
        new_car = CarManager()
        cars.append(new_car)
        loop_counter = 0
    for car in cars:
        car.move()

    # detect collision with car
    for car in cars:
        if car.distance(player) < 20:
            game_is_on = False

screen.exitonclick()
