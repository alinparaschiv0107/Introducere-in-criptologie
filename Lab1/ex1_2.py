import utils

# Ex1
print("------ EX1 --------- ")

C1 = "010101100110000101101100011010000110000101101100011011000110000100100001"
C2 = "526f636b2c2050617065722c2053636973736f727321"
C3 = "WW91IGRvbid0IG5lZWQgYSBrZXkgdG8gZW5jb2RlIGRhdGEu"

print(utils.bin_2_str(C1))
print(utils.hex_2_str(C2))
print(utils.b64decode(C3))

# Ex2
print("------ EX2 --------- ")

c1 = "000100010001000000001100000000110001011100000111000010100000100100011101000001010001100100000101"
c2 = "02030F07100A061C060B1909"
KEY = "abcdefghijkl"

c1 = utils.bin_2_str(c1)
c2 = utils.hex_2_str(c2)

Res1 = utils.strxor(c1,KEY)
Res2 = utils.strxor(c2,KEY)

print(Res1)
print(Res2)