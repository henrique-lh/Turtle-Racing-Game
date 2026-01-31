import turtle


class UI:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color(1, 1, 1)

    def update_score(self, time_elapsed, score, x, y):
        self.pen.clear()
        self.pen.setposition(x, y)
        self.pen.write(
            f"Time: {time_elapsed:5.1f}s\nScore: {score:5}",
            font=("Courier", 20, "bold"),
        )

    def show_game_over(self):
        self.pen.home()
        self.pen.write("GAME OVER", font=("Courier", 40, "bold"), align="center")