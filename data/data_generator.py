from faker import Faker

fake = Faker()


def generate_user_data():
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "phone_number": fake.numerify("##########"),
        "country": "Philippines",
        "email": fake.email(),
        "password": fake.password(
            length=10, special_chars=True, digits=True, upper_case=True, lower_case=True
        ),
    }
