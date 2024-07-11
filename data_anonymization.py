from faker import Faker

# Initialize Faker
fake = Faker()

# Function to anonymize data
def anonymize_data(data):
    anonymized_data = {}
    for key, value in data.items():
        if key == "name":
            anonymized_data[key] = fake.name()
        elif key == "address":
            anonymized_data[key] = fake.address()
        elif key == "email":
            anonymized_data[key] = fake.email()
        else:
            anonymized_data[key] = value
    return anonymized_data

# Test the data anonymization function
if __name__ == "__main__":
    data = {
        "name": "John Doe",
        "address": "123 Main St",
        "email": "johndoe@example.com",
        "phone": "555-555-5555"
    }
    anonymized_data = anonymize_data(data)
    print(f"Anonymized Data: {anonymized_data}")
