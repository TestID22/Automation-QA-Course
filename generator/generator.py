import random

from data.Person import Person
from faker import Faker

faker_en = Faker("en_US")
Faker.seed()

def generated_person():
    yield Person(
        first_name = faker_en.first_name(),
        last_name=faker_en.last_name(),
        email = faker_en.email(),
        age = random.randint(10, 89),
        salary= random.randint(8_500, 39_000),
        department= faker_en.job()[:20],  #WebTables: Departemnt field has restricted lenght
        current_address = faker_en.address(),
        permanent_address = faker_en.address()
    )





