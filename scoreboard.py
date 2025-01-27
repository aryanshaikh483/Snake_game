from turtle import Turtle
ALIGNMENT =  "center"
FONT =  ("courier", 20,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,265)
        self.color("white")
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)
    

    def update_score(self):
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GaMe OvEr",move=False, align=ALIGNMENT, font=FONT)