from turtle import  Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        randomNum = random.randint(1,6)
        if randomNum == 1 :
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            new_car.color(random.choice(COLORS))
            self.allCars.append(new_car)

    def moveCar(self):
        for car in self.allCars:
            car.backward(self.speed)
    def levelUp(self):
        self.speed += MOVE_INCREMENT
