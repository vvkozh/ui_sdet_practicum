from faker import Faker

faker = Faker()

def generate_post_code():
    return faker.random_int(0000000000, 9999999999)

