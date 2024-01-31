from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.Score = 0
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.Score}", False, align="center", font=("Arial", 17, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, align="center", font=("Arial", 17, "normal"))

    def refresh_score(self):
        self.Score += 1
        self.clear()
        self.update_score()
