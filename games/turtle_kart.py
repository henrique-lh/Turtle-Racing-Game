from turtle import Turtle, Screen
import random
import os
import time


FONT = ("Courier", 14, "bold")
ALIGN = "right"


class TurtleKart:

    def __init__(self) -> None:
        self.screen = Screen()
        self.path = os.path.join(os.path.dirname(os.path.realpath("Turtle-Racing-Game")), "assets")
    
    def config(self, colors, odds):
        self.y_positions = [-260, -172, -85, 2, 85, 172, 260]
        self.colors = colors.copy()
        self.odds = odds.copy()
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
        user_bet = kwargs["user_bet"]
        chips = kwargs['chips']
        user = kwargs['user']

        is_on = True
        while is_on:
            for turtle in self.all_turtles:
                if turtle.xcor() > 330:
                    is_on = False
                    winner = turtle.pencolor()
                    if winner == user_bet:
                        turtle.write(f"You won! {winner} turtle is winner", font=FONT, align=ALIGN)
                        user.total_chips = int(round(user.total_chips + chips * self.odds[self.colors.index(winner)]))
                    else:
                        turtle.write(f"You lost! The {winner} turtle is winner", font=FONT, align=ALIGN)
                    break 
                random_pace = random.randint(0, 30)
                turtle.forward(random_pace)
        self.destroy() 

    def destroy(self):
        try:
            time.sleep(1)
            self.screen.reset()
        except Exception as e:
            print("Deu erro pai")

