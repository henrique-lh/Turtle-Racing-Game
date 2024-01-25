from faker import Faker 
import random 
import string
from unidecode import unidecode

fake = Faker(["pt_BR"])

def generate_fake_user_data():
    name = fake.name()
    return {
        "name": name,
        "total_chips": str(random.randint(1, 300)),
        "email": "".join(unidecode(letter) for letter in name.lower() if letter != " ") + "@ex.com",
        "phone": "".join(str(random.randint(0, 9)) for _ in range(11))
    }


def generate_ids():
    chars = string.ascii_lowercase + string.digits
    return "".join(chars[random.randint(0, 35)] for _ in range(6))


