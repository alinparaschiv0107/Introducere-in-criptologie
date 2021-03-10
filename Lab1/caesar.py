alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 
def caesar_enc(letter, k = 3):
    if letter < 'A' or letter > 'Z':
        print('Invalid letter')
        return None
    else:
        return alphabet[(ord(letter) - ord('A') + k) % len(alphabet)]
 
def caesar_dec(letter,k = 3):
    if letter < 'A' or letter > 'Z':
        print('Invalid letter')
        return
    else:
        return alphabet[(ord(letter) - ord('A') - k) % len(alphabet)]

def caesar_enc_string(plaintext, k = 3):
    ciphertext = ''
    for letter in plaintext:
        ciphertext = ciphertext + caesar_enc(letter, k )
    return ciphertext

def caesar_dec_string(plaintext, k = 3):
    deciphertext = ''
    for letter in plaintext:
        deciphertext = deciphertext + caesar_dec(letter, k )
    return deciphertext

 
def main():
    m = 'BINEATIVENIT'
    m2 = 'ELQHDWLYHQLW'
    
    c = caesar_enc_string(m,5)
    c2 = caesar_dec_string(c,5)
    
    print(c)
    print(c2)
 
if __name__ == "__main__":
    main()