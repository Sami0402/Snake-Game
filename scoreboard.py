import turtle

class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # Reading highscore from data.txt
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()



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

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.high_score}", align="center", font=("Helvetica", 15, "normal"))



