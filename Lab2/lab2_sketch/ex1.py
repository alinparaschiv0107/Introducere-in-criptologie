from caesar import *

def decrypt(ciphertext):
    plaintext = ''
    key = 0

    # for i in range(len(ciphertext) - 2):
    #     if (  ord(ciphertext[i]) - ord(ciphertext[i + 1]) == ord('Y') - ord('O') 
    #             and
    #           ord(ciphertext[i + 1]) - ord(ciphertext[i + 2]) == ord('O') - ord('U')
    #         ):
    #         key = ord(ciphertext[i]) - ord('Y')
    #         break

    # plaintext = caesar_dec_string(ciphertext, key)
    # return plaintext

    for i in range(26):
        print(caesar_dec_string(ciphertext, i+1))

def main():
    ciphertexts = []
    with open("msg_ex1.txt", 'r') as f:
        for line in f:
            ciphertexts.append(line[:-1])
    for c in ciphertexts:
        decrypt(c)
        print("\n")


if __name__ == "__main__":
    main()
