from format_funcs import *


def main():

    # Plaintexts
    s1 = 'floare'
    s2 = 'albina'
    cipherText = '021e0e061d1694c9'

    # Obtain crc of s1
    # See this site:
    # http://www.lammertbies.nl/comm/info/crc-calculation.html
    x1 = str_2_hex(s1)
    x2 = str_2_hex(s2)
    print("x1: " + x1)
    print("x2: " + x2)

    crc1 = '8E31'  # CRC-16 of x1
    crc2 = '54BA'

    # Compute delta (xor) of x1 and x2:
    xd = hexxor(x1, x2)
    crcd = hexxor(crc1, crc2)
    
    print("xd: " + xd)
    print("crcd: " + crcd)

    cipher2 = xd + crcd
    print("cipher: " + cipher2)

    res = hexxor(cipherText, cipher2)
    key = hexxor(cipherText, str_2_hex(s1) + crc1)
    decodedText = hexxor(res,key)

    print( decodedText )


if __name__ == "__main__":
    main()
