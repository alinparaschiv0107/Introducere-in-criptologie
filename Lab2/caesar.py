alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def caesar_enc(letter, k=3):
    if letter < 'A' or letter > 'Z':
        print('Invalid letter')
        return
    else:
        return alphabet[(ord(letter) - ord('A') + k) % len(alphabet)]


def caesar_dec(letter, k=3):
    if letter < 'A' or letter > 'Z':
        print('Invalid letter')
        return
    else:
        return alphabet[(ord(letter) - ord('A') - k) % len(alphabet)]


def caesar_enc_string(plaintext, k=3):
    ciphertext = ''
    for letter in plaintext:
        ciphertext = ciphertext + caesar_enc(letter, k)
    return ciphertext


def caesar_dec_string(plaintext, k=3):
    ciphertext = ''
    for letter in plaintext:
        ciphertext = ciphertext + caesar_dec(letter, k)
    return ciphertext
