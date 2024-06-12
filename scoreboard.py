# Create a class to keep the score and end the game
from turtle import Turtle

FONT = ("Comic Sans MS", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.next_level()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Comic Sans MS", 40, "bold"))
    
    def curr_level(self):
        self.clear()
        self.goto(-280, 265)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def next_level(self):
        self.curr_level()
        self.level += 1
        
