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
        mobile_number = faker_en.numerify(text='##########'), #text = creats number with digits only
        department= faker_en.job()[:20],  #WebTables: Departemnt field has restricted lenght
        current_address = faker_en.address(),
        permanent_address = faker_en.address()
    )


def file_generator():
    path = rf"D:\Automation\Automation-QA-Course\filetest{random.randint(1, 1000000)}"
    file = open(path, "+w")
    file.write("Are you kidding me?")
    file.close()
    return path, file.name


