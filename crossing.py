import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)

# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Call the neccessary functions
player = Player()
cars = CarManager()
score = Scoreboard()

# The player can only move forward
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    # Add new cars
    cars.create_car()
    cars.move()
    
    #Detect collision with a car
    for car in cars.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False
    
    #Go to a new level, increase the speed of the "cars"       
    if player.ycor() > 280:
        score.next_level()
        player.goto(STARTING_POSITION)
        cars.speed_up()

screen.exitonclick()