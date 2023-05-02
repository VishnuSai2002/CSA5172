import string
def polyalphabetic_encrypt(plain_text, key):
    alphabet = string.ascii_lowercase
    key_index = 0
    cipher_text = ''    
    for char in plain_text.lower():
        if char not in alphabet:
            cipher_text += char
        else:
            key_char = key[key_index % len(key)].lower()
            shift = alphabet.index(key_char)
            cipher_char = alphabet[(alphabet.index(char) + shift) % len(alphabet)]
            cipher_text += cipher_char
            key_index += 1    
    return cipher_text
def polyalphabetic_decrypt(cipher_text, key):
    alphabet = string.ascii_lowercase
    key_index = 0
    plain_text = ''    
    for char in cipher_text.lower():
        if char not in alphabet:
            plain_text += char
        else:
            key_char = key[key_index % len(key)].lower()
            shift = alphabet.index(key_char)
            plain_char = alphabet[(alphabet.index(char) - shift) % len(alphabet)]
            plain_text += plain_char
            key_index += 1    
    return plain_text
key = input("Enter Key:")
message = input("Enter PlainText:")
cipher_text = polyalphabetic_encrypt(message, key)
print('Cipher text:', cipher_text)
plain_text = polyalphabetic_decrypt(cipher_text, key)
print('Plain text:', plain_text)
