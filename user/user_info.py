from dataclasses import dataclass
import re
from utils.generate_data import generate_ids
import os
import csv


@dataclass
class User:

    """A class to hold a user's data."""

    name: str
    total_chips: float
    email: str
    phone: str
    card: str = ""

    def __post_init__(self):
        """Validate entries"""
        if not self.validate_email():
            print("erro no email")
            raise ValueError("Email não é válido")

        if not self.validate_phone_number():
            print("erro no número")
            raise ValueError("Telefone em formato inadequado")

        if not self.card:
            self.card = generate_ids()
    
    def validate_email(self):
        """Validate email"""
        pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return pattern.match(self.email)
    
    def validate_phone_number(self):
        """Validate phone number"""
        pattern = re.compile(r'\(\d{2}\) \d{5}-\d{4}$')
        pattern2 = re.compile(r'^\d{11}$')
        return pattern.match(self.phone) or pattern2.match(self.phone)

    def bet(self, chips):
        """Bet in a game"""
        if self.total_chips - chips < 0:
            raise ValueError(f"Não é possível apostar. Suas fichas: {self.total_chips}")
        self.total_chips -= chips

    @classmethod
    def from_code(cls, code: str):
        csv_path = os.path.join(os.path.dirname(os.path.realpath("Turtle-Racing-Game")), "results")
        csv_file = os.path.join(csv_path, "result.csv")
        with open(csv_file, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == code:
                    print("retornei")
                    return cls(name=row[1], email=row[2], phone=row[3], total_chips=round(float(row[4]), 2), card=row[0])
        raise ValueError("code not found")

