from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Player:
    
    _name: str
    _age: int
    _initial_value: float
    _bet_value: float = None
    _bet_color: str = None


    @classmethod
    def get_user_input(cls) -> Player:
        print("Registering new player...\n")
        new_name = input("Enter your name: ")
        new_age = int(input("Enter your age: "))
        new_amount = float(input("Register a value to enter the cassino: ")) * 100
        return cls(new_name, new_age, new_amount)

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def bet_color(self) -> str:
        return self._bet_color

    @bet_color.setter
    def bet_color(self, new_color: str) -> None:
        self._bet_color = new_color

    @property
    def inital_value(self) -> float:
        return self._initial_value

    @inital_value.setter
    def initial_value(self, new_value: float) -> None:
        self._initial_value = new_value

    @property
    def bet_value(self) -> float:
        return self._bet_value

    @bet_value.setter
    def bet_value(self, new_value: float) -> None:
        self._bet_value = new_value
