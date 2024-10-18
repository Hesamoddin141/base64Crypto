import base64

# Function to encode using Base64
def base64_encrypt(plaintext):
    encoded_text = base64.b64encode(plaintext.encode()).decode()  # Encode the plaintext and convert bytes to string
    return encoded_text

# Function to decode from Base64
def base64_decrypt(encoded_text):
    decoded_text = base64.b64decode(encoded_text).decode()  # Decode the Base64 string and convert bytes to string
    return decoded_text

# Main program
if __name__ == "__main__":
    choice = input("Choose 'encrypt' to encode or 'decrypt' to decode: ").lower()
    if choice == 'encrypt':
        plaintext = input("Enter the text to encrypt: ")
        print("Encoded Text:", base64_encrypt(plaintext))
    elif choice == 'decrypt':
        encoded_text = input("Enter the Base64 encoded text to decrypt: ")
        print("Decoded Text:", base64_decrypt(encoded_text))
    else:
        print("Invalid choice!")
