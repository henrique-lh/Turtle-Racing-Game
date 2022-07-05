from typing import List, TypeVar
import random
import time

PLAYER = TypeVar('PLAYER')
RACER = TypeVar('RACER')


class Game:

    """Class that represents the game"""

    def start(self, all_racers: List[RACER], user: PLAYER) -> str:
        """Start a new game

        Args:
            all_racers (List[RACER]): List of racers present in the race
            user (PLAYER): Player who plays the game

        Returns:
            str: Color of the winner turtle
        """
        is_on = True

        while is_on:
            for turtle in all_racers:
                random_pace = random.randint(0, 30)
                turtle.racer.forward(random_pace)
                if turtle.racer.xcor() > 330:
                    winner = turtle.racer.pencolor()
                    self.display_winner(user, winner, turtle)
                    turtle.add_victory()
                    is_on = False
                    break
        time.sleep(4)
        turtle.racer.clear()
        return winner

    def display_winner(self, user: PLAYER, winner: str, turtle: RACER) -> None:
        """Display in the screen the winner of the race

        Args:
            user (PLAYER): Player who plays the game
            winner (str): Color of the winner turtle
            turtle (RACER): The winner turtle object
        """
        ALIGN = "right"
        FONT = ("Courier", 15, "bold")
        default = ""
        if winner == user.bet_color:
            default = "YOU WON!"
        else:
            default = "YOU LOSE!"
        turtle.racer.write(f"{default} The {winner} turtle is winner!", font=FONT, align=ALIGN)
