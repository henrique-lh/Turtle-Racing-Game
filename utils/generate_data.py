from faker import Faker 
import random 
import string
from unidecode import unidecode

fake = Faker(["pt_BR"])

def generate_fake_user_data():
    name = fake.name()
    return {
        "name": name,
        "total_chips": str(random.randint(100, 1000)),
        "email": "".join(unidecode(letter) for letter in name.lower() if letter != " ") + "@ex.com",
        "phone": "".join(str(random.randint(0, 9)) for _ in range(11))
    }


def generate_ids():
    pw = [string.ascii_lowercase[random.randint(0, 25)] if i % 2 == 0 else string.digits[random.randint(0, 9)] for i in range(6)]
    random.shuffle(pw)
    return "".join(pw)

