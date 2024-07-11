import os
from cryptography.fernet import Fernet
import getpass

# Define the storage directory and its size limit
STORAGE_DIR = "personal_storage"
STORAGE_SIZE_LIMIT = 25 * 1024 * 1024 * 1024  # 25GB

# Function to check if the storage size is within the limit
def check_storage_size():
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(STORAGE_DIR):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size <= STORAGE_SIZE_LIMIT

# Function to initialize the storage
def initialize_storage(password):
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    key = Fernet.generate_key()
    with open(os.path.join(STORAGE_DIR, "key.key"), "wb") as key_file:
        key_file.write(key)
    with open(os.path.join(STORAGE_DIR, "password.txt"), "wb") as password_file:
        password_file.write(Fernet(key).encrypt(password.encode()))

# Function to load the encryption key
def load_key():
    return open(os.path.join(STORAGE_DIR, "key.key"), "rb").read()

# Function to authenticate the user
def authenticate(password):
    key = load_key()
    fernet = Fernet(key)
    stored_password = open(os.path.join(STORAGE_DIR, "password.txt"), "rb").read()
    return fernet.decrypt(stored_password).decode() == password

# Function to encrypt and store data
def store_encrypted_data(filename, data, password):
    if authenticate(password):
        key = load_key()
        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data.encode())
        with open(os.path.join(STORAGE_DIR, filename), "wb") as file:
            file.write(encrypted_data)
        if not check_storage_size():
            os.remove(os.path.join(STORAGE_DIR, filename))
            raise Exception("Storage limit exceeded.")
    else:
        raise Exception("Authentication failed.")

# Function to decrypt and retrieve data
def retrieve_encrypted_data(filename, password):
    if authenticate(password):
        key = load_key()
        fernet = Fernet(key)
        with open(os.path.join(STORAGE_DIR, filename), "rb") as file:
            encrypted_data = file.read()
        return fernet.decrypt(encrypted_data).decode()
    else:
        raise Exception("Authentication failed.")

# Test the storage functions
if __name__ == "__main__":
    password = getpass.getpass("Set storage password: ")
    initialize_storage(password)

    test_password = getpass.getpass("Enter storage password: ")
    if authenticate(test_password):
        store_encrypted_data("test.txt", "This is a test.", test_password)
        data = retrieve_encrypted_data("test.txt", test_password)
        print(f"Retrieved Data: {data}")
    else:
        print("Authentication failed.")
