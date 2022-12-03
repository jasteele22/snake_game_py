from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.ht()
        self.penup()
        self.setposition(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score} High Score: {self.high_score}", align="center", font=('Courier', 16, "normal"))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0

    def game_over(self  ):
        self.setposition(0, 0)
        self.write("GAME OVER", align= 'center',font=('Courier', 48, "bold"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
