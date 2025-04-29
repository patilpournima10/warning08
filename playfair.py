def prepare_key(key):
    key = key.upper().replace('J', 'I')
    key = ''.join(dict.fromkeys(key))  # Remove duplicates
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    key += ''.join(c for c in alphabet if c not in key)
    matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
    return matrix

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)

def prepare_text(plaintext):
    plaintext = plaintext.upper().replace('J', 'I')
    pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = 'X' if i + 1 == len(plaintext) or plaintext[i] == plaintext[i + 1] else plaintext[i + 1]
        pairs.append(a + b)
        i += 2 if a != b else 1
    return pairs

def encrypt(plaintext, matrix):
    pairs = prepare_text(plaintext)
    ciphertext = ''
    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    return ciphertext

def decrypt(ciphertext, matrix):
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    return plaintext

def main():
    key = input("Enter secret key: ")
    plaintext = input("Enter plaintext: ")
    matrix = prepare_key(key)

    print("\nKey Matrix:")
    for row in matrix:
        print(' '.join(row))

    encrypted_text = encrypt(plaintext, matrix)
    print(f"\nEncrypted Text: {encrypted_text}")
    decrypted_text = decrypt(encrypted_text, matrix)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
