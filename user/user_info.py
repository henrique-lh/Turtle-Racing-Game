from dataclasses import dataclass
import re
from utils.generate_data import generate_ids


@dataclass
class User:

    """A class to hold a user's data."""

    name: str
    total_chips: int
    email: str
    phone: str

    def __post_init__(self):
        """Validate entries"""
        if not self.validate_email():
            raise ValueError("Email não é válido")

        if not self.validate_phone_number():
            raise ValueError("Telefone em formato inadequado")

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

