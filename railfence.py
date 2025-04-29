def rail_fence_encrypt(plaintext, depth): 
    if depth <= 1: 
        return plaintext 
    rails = ['' for _ in range(depth)] 
    row, direction = 0, 1 
 
    for char in plaintext: 
        rails[row] += char 
        if row == 0: 
            direction = 1 
        elif row == depth - 1: 
            direction = -1 
        row += direction 
 
    return ''.join(rails) 
 
def rail_fence_decrypt(ciphertext, depth): 
    if depth <= 1: 
        return ciphertext 
 
    rails = ['' for _ in range(depth)] 
    row, direction = 0, 1 
    pattern = ['' for _ in ciphertext] 
 
    # Create pattern to mark the rails 
    for i in range(len(ciphertext)): 
        pattern[i] = row 
        if row == 0: 
            direction = 1 
        elif row == depth - 1: 
            direction = -1 
        row += direction 
 
    index = 0 
    for r in range(depth): 
        for i in range(len(ciphertext)): 
            if pattern[i] == r: 
                rails[r] += ciphertext[index] 
                index += 1 
 
    row, direction = 0, 1 
    plaintext = '' 
 
    for i in range(len(ciphertext)): 
        plaintext += rails[row][0] 
        rails[row] = rails[row][1:] 
        if row == 0: 
            direction = 1 
        elif row == depth - 1: 
            direction = -1 
        row += direction 
 
    return plaintext 
 
# Example usage 
plaintext = "HELLO WORLD" 
depth = 3 
 
encrypted_text = rail_fence_encrypt(plaintext, depth) 
print("Encrypted Text:", encrypted_text) 
decrypted_text = rail_fence_decrypt(encrypted_text, depth) 
print("Decrypted Text:", decrypted_text) 
