import turtle
from abc import ABC, abstractmethod


class Game(ABC):
    """Abstract base class for any game."""

    def __init__(self):
        self.window = turtle.Screen()
        self.game_running = False

    @abstractmethod
    def config(self):
        """Setup screen, keybindings, and initial state."""
        pass

    @abstractmethod
    def play(self):
        """Main game loop."""
        pass
