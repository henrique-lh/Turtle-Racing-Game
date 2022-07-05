from __future__ import annotations
from dataclasses import dataclass
from registerWindow import RegisterWindow
import csv
from typing import List

@dataclass
class Player:

    """Class that represents a player"""
    
    _name: str
    _age: int
    _initial_value: float
    _bet_value: float = None
    _bet_color: str = None


    @classmethod
    def cli_input(cls) -> Player:
        """Get user data from a commando line interface

        Returns:
            Player: return a new player
        """

        print("Registering new player...\n")
        new_name = input("Enter your name: ")
        new_age = int(input("Enter your age: "))
        new_amount = float(input("Register a value to enter the cassino: ")) * 100
        return cls(new_name, new_age, new_amount)

    @classmethod
    def csv_input(cls) -> Player:
        """Get user data from csv file

        Returns:
            Player: return a new player
        """

        with open('data.csv') as csv_file:
            csv_reader  = csv.reader(csv_file, delimiter=',')
            data = list(csv_reader)

        new_name, new_age, new_amount = data[0][0], int(data[0][1]), float(data[0][2]) * 100
        return cls(new_name, new_age, new_amount)

    @property
    def name(self) -> str:
        """Get user name"""

        return self._name

    @property
    def age(self) -> int:
        """Get the user age"""

        return self._age

    @property
    def bet_color(self) -> str:
        """Get the turtle color bet by user"""

        return self._bet_color

    @bet_color.setter
    def bet_color(self, new_color: str) -> None:
        """Set the turtle color bet by user"""

        self._bet_color = new_color

    @property
    def inital_value(self) -> float:
        """Get the current value that the player owns"""

        return self._initial_value

    @inital_value.setter
    def initial_value(self, new_value: float) -> None:
        """Set the current value that the player owns"""

        self._initial_value = new_value

    @property
    def bet_value(self) -> float:
        """Get the bet value"""

        return self._bet_value

    @bet_value.setter
    def bet_value(self, new_value: float) -> None:
        """Set the bet value"""

        self._bet_value = new_value
