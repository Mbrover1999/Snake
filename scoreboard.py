from turtle import Turtle


class Scoreboard(Turtle):
    score = 0
    with open("data.txt", mode="r") as file:
        content = file.read()
        
    high_score = int(content)

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def addScore(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", font=('Arial', 20, 'normal'),
                   align="center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.update_scoreboard()
