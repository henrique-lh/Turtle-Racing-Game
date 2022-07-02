from turtle import Screen, TurtleScreen
from typing import Dict
from player import Player
from game import Game
from racer import setup_racers, COLORS
import os
from prettytable import PrettyTable


def config_log() -> PrettyTable:
    """Return a configured PrettyTable object"""

    table = PrettyTable()
    table.field_names = ["Your bet", "Value", "Result"]
    table.align["Your bet"] = "l"
    table.align["Value"] = "r"
    return table

def lines() -> None:
    """Print lines

        Default: Print a line with 50 of length.
    """

    print('-' * 50)

def show_possible_colors():
    """Print the possible color that can be choosen by the user"""

    for index, color in enumerate(COLORS):
        print(f"{index + 1} - {color}")
    print()

class Machine:

    _new_game = Game()
    _all_racers = setup_racers()
    _log: Dict[str, PrettyTable] = dict()
    _player: Player = None


    def __init__(self) -> None:
        self.screen = Screen()
        TurtleScreen._RUNNING = True
        self.screen.setup(width=800, height=600)
        self.screen.bgpic('road.gif')

    def start_machine(self) -> None:
        Machine._player = self.register_new_player()
        playing = self.play()
        while playing:
            winner = Machine._new_game.start(Machine._all_racers, Machine._player)
            self.add_log(winner)
            if self.play():
                self.positioning()
            else:
                playing = False
                self.screen.bye()
        self.get_statistics()

    def register_new_player(self) -> Player:
        local_player = Player.get_user_input()
        Machine._log[local_player.name] = config_log()
        return local_player

    def get_statistics(self) -> None:
        os.system('clear')

        print(f"{'REGISTER':^28}")
        print(f"Name: {Machine._player.name.capitalize():<22}")
        print(f"Age: {Machine._player.age:<22}")
        cash_format = f"{(Machine._player.inital_value / 100):.2f}"
        print(f"Cash: $ {cash_format:<21}")
        print()
        print(f"{'Bets':^33}")
        print(Machine._log[Machine._player.name])

    def play(self) -> bool:
        os.system('clear')
        lines()
        print("Do you wanna play the game?\nYES - 1\tNO - 2\n")
        keep_game = int(input())
        if keep_game == 1:
            print('New color bet. Choose a color:')
            show_possible_colors()
            color = int(input()) - 1
            Machine._player.bet_color = COLORS[color]
            Machine._player.bet_value = float(input('Value bet: ')) * 100
            return True
        return False

    def add_log(self, winner: str) -> None:
        result = ""

        if winner == Machine._player.bet_color:
            Machine._player.initial_value = Machine._player.initial_value + Machine._player.bet_value
            result = "WINNER"
        else:
            Machine._player.initial_value = Machine._player.initial_value - Machine._player.bet_value
            result = "LOSER"

        row = [[Machine._player.bet_color, Machine._player.bet_value / 100, result]]
        Machine._log[Machine._player.name].add_rows(row)

    def positioning(self) -> None:
        y_positions = [-260, -172, -85, 2, 85, 172, 260]
        for index, turtle in enumerate(Machine._all_racers):
            turtle.reposition_racer(y_positions[index])
