from dataclasses import dataclass, field
from games import GameInterface
from user import User
import json 


@dataclass 
class Result:

    user: list[User] = field(default_factory=list) 
    game: list[GameInterface] = field(default_factory=list)

    def write_data(self):
        pass

    def retrieve_data(self, code: str):
        pass

