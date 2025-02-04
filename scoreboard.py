from turtle import Turtle


ALIGNMENT =  "center"
FONT =  ("courier", 20,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.goto(0,265)
        self.color("white")
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)
    

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GaMe OvEr",move=False, align=ALIGNMENT, font=FONT)