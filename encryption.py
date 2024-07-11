from cryptography.fernet import Fernet

# Function to generate a key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt data
def encrypt_data(data, key):
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()

# Test the encryption functions
if __name__ == "__main__":
    key = generate_key()
    data = "This is a secret message."
    encrypted_data = encrypt_data(data, key)
    print(f"Encrypted: {encrypted_data}")
    decrypted_data = decrypt_data(encrypted_data, key)
    print(f"Decrypted: {decrypted_data}")
