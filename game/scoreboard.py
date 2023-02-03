from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier',20,'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.ht()
        self.penup()
        self.score = 0
        self.setpos(0,370)
    #Displays Score    
    def displayScore(self):
        self.clear()
        self.write(f'Score: {self.score}',False,align=ALIGNMENT,font=FONT)
    
    #Game over text
    def gameover(self):
        self.goto(0,0)
        self.write(f'GAME OVER :(',False,align=ALIGNMENT,font=FONT)
        