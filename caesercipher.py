alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_cipher_encrypt(plain_text, shift, alphabet_lower, alphabet_upper):
    encrypted_text = ""

    for char in plain_text:
        if char in alphabet_lower:
            position = alphabet_lower.index(char)
            new_position = (position + shift) % 26
            encrypted_text += alphabet_lower[new_position]
        elif char in alphabet_upper:
            position = alphabet_upper.index(char)
            new_position = (position + shift) % 26
            encrypted_text += alphabet_upper[new_position]
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(cipher_text, shift, alphabet_lower, alphabet_upper):
    decrypted_text = ""

    for char in cipher_text:
        if char in alphabet_lower:
            position = alphabet_lower.index(char)
            new_position = (position - shift) % 26
            decrypted_text += alphabet_lower[new_position]
        elif char in alphabet_upper:
            position = alphabet_upper.index(char)
            new_position = (position - shift) % 26
            decrypted_text += alphabet_upper[new_position]
        else:
            decrypted_text += char
    return decrypted_text

# Main Program
choice = input("Do you want to encrypt or decrypt? (Enter 'encrypt' or 'decrypt'): ").strip().lower()
text = input("Enter the text: ")
shift_value = int(input("Enter the shift value: "))

if choice == 'encrypt':
    result = caesar_cipher_encrypt(text, shift_value, alphabet_lower, alphabet_upper)
    print("Encrypted text:", result)
elif choice == 'decrypt':
    result = caesar_cipher_decrypt(text, shift_value, alphabet_lower, alphabet_upper)
    print("Decrypted text:", result)
else:
    print("Invalid choice! Please enter 'encrypt' or 'decrypt'.")
