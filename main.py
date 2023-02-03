import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
scoreboard = Scoreboard()
player = Player()
carManager = CarManager()
screen.onkey(player.up,"w")
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_car()
    carManager.moveCar()

    #collision
    for car in carManager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.gameOver()

    #detect a success
    if player.isAtFinishLine():
        player.goToStart()
        carManager.levelUp()
        scoreboard.increseScore()


screen.exitonclick()