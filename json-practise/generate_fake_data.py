from faker import Faker
import json

# Initialize Faker instance
fake = Faker()

# Generate fake data
data = []
for _ in range(10):  # You can adjust the range to generate more or fewer records
    person = {
        "name": fake.name(),
        "address": fake.address(),
        "email": fake.email(),
        "phone_number": fake.phone_number(),
        "job": fake.job(),
        "company": fake.company(),
        "birthdate": fake.date_of_birth().isoformat(),
    }
    data.append(person)

# Write the data to a JSON file
with open('data.JSON', 'w') as output:
    json.dump(data, output, indent=4)

print("Fake JSON data written to 'data.JSON'")
