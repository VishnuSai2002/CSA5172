import random


def encrypt(plaintext, key):
    ciphertext = ""
    key_length = len(key)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            char_value = ord(char.upper()) - ord('A')
            key_value = key[i % key_length]
            encrypted_value = (char_value + key_value) % 26
            encrypted_char = chr(encrypted_value + ord('A'))
            ciphertext += encrypted_char
        else:
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""
    key_length = len(key)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            char_value = ord(char.upper()) - ord('A')
            key_value = key[i % key_length]
            decrypted_value = (char_value - key_value) % 26
            decrypted_char = chr(decrypted_value + ord('A'))
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext



plaintext = "HELLO WORLD"
key = [3, 19, 5]

ciphertext = encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_text = decrypt(ciphertext, key)
print("Decrypted text:", decrypted_text)
