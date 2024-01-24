from .game import GameInterface
from turtle import Turtle, Screen, screensize
import random
import os


FONT = ("Courier", 14, "bold")
ALIGN = "right"


class TurtleKart(GameInterface):

    def __init__(self) -> None:
        super().__init__()
    
    def config(self):
        self.y_positions = [-260, -172, -85, 2, 85, 172, 260]
        self.colors = ["white", "red", "orange", "pink", "tomato", "dodgerblue", "yellow"]
        self.all_turtles = []
        self.screen.setup(width=800, height=600)
        self.screen.bgpic(os.path.join(self.path, "road.gif"))

        for index in range(7):
            new_tur = Turtle(shape="turtle")
            new_tur.shapesize(2)
            new_tur.speed('fastest')
            new_tur.penup()
            new_tur.goto(x=-350, y=self.y_positions[index])
            new_tur.color(self.colors[index])
            self.all_turtles.append(new_tur)
 
    def play(self, **kwargs):
        is_on = True
        while is_on:
            for turtle in self.all_turtles:
                if turtle.xcor() > 330:
                    is_on = False
                    winner = turtle.pencolor()
                    if winner == kwargs["user_bet"]:
                        turtle.write(f"You won! {winner} turtle is winner", font=FONT, align=ALIGN)
                    else:
                        turtle.write(f"You lost! The {winner} turtle is winner", font=FONT, align=ALIGN)
                random_pace = random.randint(0, 30)
                turtle.forward(random_pace)

        self.screen.exitonclick()

    def repeat(self):
        pass

    def destroy(self):
        pass

