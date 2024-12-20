# By: Mohaned Salaheldin
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Function to encrypt using DES
def encrypt_des(text, key):
    # Create a DES cipher object with the given key
    cipher = DES.new(key, DES.MODE_ECB)
    # Pad the text to ensure it's a multiple of 8 bytes
    padded_text = text.ljust(8 * ((len(text) + 7) // 8))
    # Encrypt the text and return the encrypted data
    encrypted_data = cipher.encrypt(padded_text.encode())
    return encrypted_data

# Function to decrypt using DES
def decrypt_des(encrypted_data, key):
    # Create a DES cipher object with the given key
    cipher = DES.new(key, DES.MODE_ECB)
    # Decrypt the data and strip any padding spaces
    decrypted_text = cipher.decrypt(encrypted_data).decode().strip()
    return decrypted_text

# Main example
if __name__ == "__main__":
    # Generate a random 8-byte (64-bit) encryption key
    key = get_random_bytes(8)
    
    # Original text to be encrypted
    original_text = "HelloDES"

    # Encrypt the original text
    encrypted_text = encrypt_des(original_text, key)
    print("Encrypted text:", encrypted_text)

    # Decrypt the text back to original
    decrypted_text = decrypt_des(encrypted_text, key)
    print("Decrypted text:", decrypted_text)
