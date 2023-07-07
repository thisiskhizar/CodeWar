def encrypt_message(message):
    encrypted_message = ""
    for char in message:
        if 'A' <= char <= 'N' or 'a' <= char <= 'n':
            encrypted_message += "*f"
        elif 'O' <= char <= 'Z' or 'o' <= char <= 'z':
            encrypted_message += "#b"
        elif '0' <= char <= '5':
            encrypted_message += "@N1"
        elif '6' <= char <= '9':
            encrypted_message += "&N2"
        else:
            encrypted_message += "No"
    return encrypted_message


def decrypt_message(encrypted_message):
    pass


# Example usage
message = "personName_0198"
output = encrypt_message(message)
print("Encrypted message: ", output)
