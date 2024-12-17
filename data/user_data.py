from faker import Faker


fake = Faker()

USER_DATA = {
    "name": fake.name(),
    "email": fake.email(),
    "title": str(fake.random_int(1, 2)),
    "password": fake.password(),
    "birth_day": str(fake.random_int(1, 28)),
    "birth_month": str(fake.random_int(1, 12)),
    "birth_year": str(fake.random_int(1900, 2021)),
    "company": fake.company(),
    "address1": fake.address(),''
    "address2": fake.secondary_address(),
    "country": "United States",
    "state": fake.state_abbr(),
    "city": fake.city(),
    "zipcode": fake.zipcode(),
    "mobile_number": fake.basic_phone_number()
}
