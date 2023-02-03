import turtle as t
import random

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed(0)
        self.move_food()
    #Spawns food on a random location
    def move_food(self):
        random_x = (random.randint(-380,380))
        random_y = (random.randint(-380,380))
        self.setpos((random_x,random_y))
        
        
        
        