from turtle import Turtle
import random

# Random colors for new cars
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()  
    
    # Create a car and assign a color to it    
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            new_car.setposition(300, random.randint(-260, 280))
            self.all_cars.append(new_car)
    
    # Set the distance traversed with each move    
    def move(self):
        for car in self.all_cars:
            car.x_move = STARTING_MOVE_DISTANCE
            #new_x = self.xcor() + self.x_move
            car.forward(self.car_speed)
        
    def speed_up(self):
        self.car_speed += MOVE_INCREMENT
        
        
