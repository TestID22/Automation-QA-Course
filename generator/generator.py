from data.Person import Person
from faker import Faker

faker_en = Faker("en_US")
Faker.seed()

def generated_person():
    yield Person(
        full_name = faker_en.name(),
        email = faker_en.email(),
        current_address = faker_en.address(),
        permanent_address = faker_en.address()
    )