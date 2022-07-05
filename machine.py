from turtle import Screen, TurtleScreen
from player import Player
from game import Game
from racer import setup_racers, COLORS
import os
from prettytable import PrettyTable, DOUBLE_BORDER


def config_log() -> PrettyTable:
    """Return a configured PrettyTable object"""

    table = PrettyTable()
    table.set_style(DOUBLE_BORDER)

    table.field_names = ["Your bet", "Value", "Result"]
    table.align["Your bet"] = "l"
    table.align["Value"] = "r"
    return table

def lines() -> None:
    """Print lines

        Default: Print a line with 50 of length.
    """

    print('-' * 50)

def show_possible_colors() -> None:
    """Print the possible color that can be choosen by the user"""

    def colored(r, g, b, text) -> str:
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

    rgb_code = {
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'orange': (255, 127, 0),
        'pink': (255, 182, 193),
        'tomato': (238, 92, 66),
        'dodgerblue': (30, 144, 255),
        'yellow': (255, 255, 0)
    }

    for index, color in enumerate(COLORS):
        text = f"{index + 1} - {color}"
        colored_text = colored(*rgb_code[color], text)
        print(colored_text)
    print()

class Machine:

    """Class that represents the machine"""

    _log: PrettyTable = config_log()
    _player: Player = None

    def __init__(self) -> None:
        self._all_racers = setup_racers()
        self.screen = Screen()
        TurtleScreen._RUNNING = True
        self.screen.setup(width=800, height=600)
        self.screen.bgpic('road.gif')
        self._new_game = Game()

    def start_machine(self) -> None:
        """Turns on the machine. Then, a new player is added and the game start"""
        Machine._player = Player.csv_input()
        playing = self.play()
        while playing:
            winner = self._new_game.start(self._all_racers, Machine._player)
            self.add_log(winner)
            if self.play():
                self.positioning()
            else:
                playing = False
                self.screen.bye()
        self.get_statistics()

    def get_statistics(self) -> None:
        """Get the statistics of the player"""

        os.system('clear')

        print(f"{'PLAYER INFO':^28}\n")
        print(f"Name: {Machine._player.name.capitalize():<22}")
        print(f"Age: {Machine._player.age:<22}")
        print(f"Email: {Machine._player.email:<22}")
        cash_format = f"{(Machine._player.inital_value / 100):.2f}"
        print(f"Cash: $ {cash_format:<21}")

        print()

        print(f"{'STATISTICS':^33}\n")
        print(Machine._log)

    def play(self) -> bool:
        """Check if the player will keep playing the game"""

        os.system('clear')
        lines()
        print("Do you wanna play the game?\nYES - 1\tNO - 2\n")

        try:
            keep_game = int(input("Enter your option: "))
        except ValueError:
            os.system('clear')
            print("Do you wanna play the game?\nYES - 1\tNO - 2\n")
            keep_game = int(input("Enter your option: "))

        if keep_game == 1:
            print('New color bet. Choose a color:')
            show_possible_colors()
            color = int(input("Enter your option: ")) - 1
            Machine._player.bet_color = COLORS[color]
            Machine._player.bet_value = float(input('Value bet: ')) * 100
            return True
        return False

    def add_log(self, winner: str) -> None:
        """Add the result of the game in a table

        Args:
            winner (str): Color of the winner turtle
        """

        result = ""

        if winner == Machine._player.bet_color:
            Machine._player.initial_value = Machine._player.initial_value + Machine._player.bet_value
            result = "WINNER"
        else:
            Machine._player.initial_value = Machine._player.initial_value - Machine._player.bet_value
            result = "LOSER"

        row = [[Machine._player.bet_color, Machine._player.bet_value / 100, result]]
        Machine._log.add_rows(row)

    def positioning(self) -> None:
        """Restart the turtle's positions"""

        y_positions = [-260, -172, -85, 2, 85, 172, 260]
        for index, turtle in enumerate(self._all_racers):
            turtle.reposition_racer(y_positions[index])
