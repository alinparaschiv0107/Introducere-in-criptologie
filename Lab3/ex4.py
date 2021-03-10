import utils
import math
import random

NUM_TESTS = 10000

#Parameters for weak LC RNG
class WeakRNG:
    "Simple class for weak RNG"
    def __init__(self,a,b):
        self.rstate = 0
        self.maxn = 255
        self.a = a
        self.b = b
        self.p = 256

    def init_state(self):
        "Initialise rstate"
        self.rstate = 0 #Set this to some value
        self.update_state()

    def update_state(self):
        "Update state"
        self.rstate = (self.a * self.rstate + self.b) % self.p

    def get_prg_byte(self):
        "Return a new PRG byte and update PRG state"
        b = self.rstate & 0xFF
        self.update_state()
        return b

def get_random_string(n):  # generate random bit string
	bstr = bin(random.getrandbits(n)).lstrip('0b').zfill(n)
	return bstr

def monobit_test(bit_seq):
	sum = 0
	for bit in bit_seq:
		if bit == '0':
			sum -= 1
		else:
			sum +=1

	return math.erfc(math.fabs(sum) / math.sqrt(100)) >= 0.01

if __name__ == "__main__":
	wr = WeakRNG(9, 6)
	count_WR = 0
	count_random = 0

	for i in range(NUM_TESTS):
		rng = b""
		for j in range(100):
			wr.update_state()
			rng += bytes([wr.rstate])

		count_WR += monobit_test(utils.hex_2_bin(rng.hex()))
		count_random += monobit_test(get_random_string(100))

	probab_WR = count_WR / NUM_TESTS
	probab_random = count_random / NUM_TESTS

	print("RNG is random - {}" .format(probab_WR))
	print("Random bits - {}" .format(probab_random))