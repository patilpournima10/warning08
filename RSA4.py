import random
from math import gcd

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_candidate(start=100, end=999):
    primes = [i for i in range(start, end) if is_prime(i)]
    return random.choice(primes)

def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_keys():
    p = generate_prime_candidate()
    q = generate_prime_candidate()
    while p == q:
        q = generate_prime_candidate()

    n = p * q
    phi = (p - 1) * (q - 1)

    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = ''.join(chr(pow(char, d, n)) for char in ciphertext)
    return plaintext

def main():
    print("RSA Encryption and Decryption")
    public_key, private_key = generate_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    plaintext = input("Enter plaintext message: ")
    encrypted_message = encrypt(plaintext, public_key)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
