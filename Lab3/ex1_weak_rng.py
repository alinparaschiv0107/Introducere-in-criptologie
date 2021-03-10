import utils

#Parameters for weak LC RNG
class WeakRNG:
    "Simple class for weak RNG"
    def __init__(self):
        self.rstate = 0
        self.maxn = 255
        self.a = 0 #Set this to correct value
        self.b = 0 #Set this to correct value
        self.p = 257

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

  
def main():

    #Initialise weak rng
    wr = WeakRNG()
    wr.init_state()

    #Print ciphertext
    CH = 'a432109f58ff6a0f2e6cb280526708baece6680acc1f5fcdb9523129434ae9f6ae9edc2f224b73a8'
    print("Full ciphertext in hexa: " + CH)

    #Print known plaintext
    pknown = 'Let all creation'
    nb = len(pknown)
    print("Known plaintext: " + pknown)
    pkh = utils.str_2_hex(pknown)
    print("Plaintext in hexa: " + pkh)

    #Obtain first nb bytes of RNG
    gh = utils.hexxor(pkh, CH[0:nb*2])
    print(gh)
    gbytes = []
    for i in range(nb):
        gbytes.append(ord(utils.hex_2_str(gh[2*i:2*i+2])))
    print("Bytes of RNG: ")
    print(gbytes)

    #Break the LCG here:
    #1. find a and b
    #2. predict/generate rest of RNG bytes
    #3. decrypt plaintext
    for a in range(257):
        for b in range(257):
            correct = True
            
            for i in range(1, 16):
                if gbytes[i] != (a * gbytes[i - 1] + b) % wr.p:
                    correct = False
                    break

            if correct:
                wr.a = a
                wr.b = b
                break

    # Print full plaintext
    p = "Let all creation"
    wr.rstate = gbytes[15]

    for i in range(16, int(len(CH) / 2)):
        wr.update_state()
        p += chr(int(CH[2*i : 2*i + 2], 16) ^ wr.rstate)
    print("Full plaintext is: " + p)


if __name__ == "__main__":
    main()  