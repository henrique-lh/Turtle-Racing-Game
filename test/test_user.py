from user import User
from utils.generate_data import generate_fake_user_data
import pytest 

def test_create_user():
    user = User(**generate_fake_user_data())
    assert user is not None

def test_check_user_id():
    user = User(**generate_fake_user_data())
    assert hasattr(user, "card")

def test_fail_user_phone():
    data = generate_fake_user_data()
    data["phone"] = "123-456-789"
    with pytest.raises(Exception) as e_info:
        user = User(**data)

def test_fail_email():
    data = generate_fake_user_data()
    data["name"] = "João"
    data["email"] = "joão@ex.com"
    with pytest.raises(Exception) as e_info:
        user = User(**data)

