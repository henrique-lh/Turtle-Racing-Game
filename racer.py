import turtle
from typing import List


class Racer:

    def __init__(self, y_position: float, color: str) -> None:
        """Constructor of the Racer class

        Args:
            y_position (float): Initial position
            color (str): Color of the racer
        """

        self._victories = 0
        self._color = color
        self._racer = turtle.Turtle('turtle')
        self._racer.shapesize(2)
        self._racer.speed('fastest')
        self._racer.penup()
        self._racer.goto(x=-350, y=y_position)
        self._racer.color(color)

    @property
    def racer(self) -> turtle.Turtle:
        """Get the racer"""

        return self._racer

    @property
    def victories(self) -> int:
        """Get the number of victories of the racer"""

        return self._victories

    @property
    def color(self) -> str:
        """Get the color of the racer"""

        return self._color

    def reposition_racer(self, new_pos: float) -> None:
        """Change the position of the racer"""

        self._racer.goto(x=-350, y=new_pos)

    def add_victory(self) -> None:
        """Add a new victory for the racer"""

        self._victories += 1


COLORS = ["white", "red", "orange", "pink", "tomato", "dodgerblue", "yellow"]

def setup_racers() -> List[Racer]:
    """Return the racers

    Returns:
        List[Racer]: Racers
    """
    number_of_racers = 7
    y_positions = [-260, -172, -85, 2, 85, 172, 260]
    all_racers = [Racer(y_positions[i], COLORS[i]) for i in range(number_of_racers)]
    return all_racers
