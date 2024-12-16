from home.models import *
from faker import Faker
import random

fake = Faker()

# def dbSeeder()->None:
#     college_names = ["MIT Muzaffarpur","NIT PATNA","IIT PATNA","NIT Trichy","NIT JamShedpur","IIT Bombay",
#                      "IIT DELHI","IIT Kanpur","IIT Roorkee","IIM INDORE"]
#     for i in college_names:
#         address = fake.address()
#         College.objects.create(college_name=i,college_address=address)

def dbSeeder(records=10)->None:
    colleges = College.objects.all()
    for i in range(records):
        college = random.choice(colleges)
        gender = random.choice(['Male','Female'])
        name = fake.name()
        mobile_number = fake.phone_number()
        email = fake.email()
        age = random.randint(18,25)
        student_bio = fake.text()

        Student2.objects.create(
            gender = gender,
            college = college,
            name = name,
            mobile_number = mobile_number,
            email = email,
            age = age,
            student_bio = student_bio
        )
        




