from turtle import Turtle

from games.kart.constants import FINISH_LINE, FONT, ALIGN


def display_winner(racer: Turtle, winner_name: str, user_choice: str) -> None:
    """Displays the victory or defeat message on the Turtle screen."""
    racer.goto(0, 0)

    if winner_name == user_choice:
        racer.write(f"YOU WON! The {winner_name} racer won!", font=FONT, align=ALIGN)
    else:
        racer.write(f"YOU LOST! The {winner_name} racer won!", font=FONT, align=ALIGN)


def check_finish_line(racer: Turtle, user_choice: str) -> bool:
    """Checks whether the turtle has crossed the line and displays the result."""
    if racer.xcor() > FINISH_LINE:
        winner_name = racer.color_name
        display_winner(racer, winner_name, user_choice)
        return False
    return True