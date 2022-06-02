import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

counter = 0
player = Player()
scoreboard = Scoreboard()

cars = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(fun=player.advance, key="space")



game_is_on = True
while game_is_on:

    cars.go_forward()
    if counter % 6 == 0:
        cars.generate_a_car()
    
    if player.ycor() > 280:
        player.goto_ini()
        scoreboard.score_update()
        cars.speed_up()
    
    for car in cars.cars_list:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    counter += 1
    time.sleep(0.1)
    screen.update()

screen.exitonclick()