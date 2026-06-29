import string
import random
from faker import Faker

class helper:

    @staticmethod
    def generate_random_first_name(length=8):
        fake = Faker()
        first_name = fake.name()
        return first_name

    @staticmethod
    def generate_random_last_name(length=8):
        fake = Faker()
        last_name = fake.name()
        return last_name

if __name__ == '__main__':
    print(f"First Name: {helper.generate_random_first_name()}")
    print(f"Last Name: {helper.generate_random_last_name()}")