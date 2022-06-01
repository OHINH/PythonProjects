from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self) -> None:
        self.cars_list = []
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.cars_speedup = MOVE_INCREMENT
        self.counter = 0
    
    def generate_a_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1,3)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.setheading(180)
        new_car.goto(300, random.randint(-260, 260))
        self.cars_list.append(new_car)
    
    def go_forward(self):
        for car in self.cars_list:
            car.forward(self.cars_speed + self.cars_speedup*self.counter)
    
    def speed_up(self):
        for car in self.cars_list:
            self.counter += 1
        
