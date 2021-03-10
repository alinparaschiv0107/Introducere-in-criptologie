from caesar import *
import math

freqs = {'A': 0.07048643054277828,
         'C': 0.01577161913523459,
         'B': 0.012074517019319227,
         'E': 0.13185372585096597,
         'D': 0.043393514259429625,
         'G': 0.01952621895124195,
         'F': 0.023867295308187673,
         'I': 0.06153403863845446,
         'H': 0.08655128794848206,
         'K': 0.007566697332106716,
         'J': 0.0017594296228150873,
         'M': 0.029657313707451703,
         'L': 0.04609015639374425,
         'O': 0.07679967801287949,
         'N': 0.060217341306347746,
         'Q': 0.0006382244710211592,
         'P': 0.014357175712971482,
         'S': 0.05892939282428703,
         'R': 0.05765294388224471,
         'U': 0.02749540018399264,
         'T': 0.09984475620975161,
         'W': 0.01892824287028519,
         'V': 0.011148804047838086,
         'Y': 0.023045078196872126,
         'X': 0.0005289788408463661,
         'Z': 0.00028173873045078196
         }

# computes the chi-distribution based on a dictionary of frequecies
# relative to the freqs frequencies dictionary

def compute_distribution(f):
    x2 = 0
    for l in freqs:
        x2 = x2 + (f[l] - freqs[l]) ** 2 / freqs[l]
    return x2

# splits a text in keylen cosets


def split_in_cosets(text, keylen):
    cosets = []
    for i in range(keylen):
        coset = []
        for j in range(i, len(text), keylen):
            coset.append(text[j])
        cosets.append(coset)
    return cosets

# merges the cosets to obtain the original text
def merge_cosets(cosets, coset_size):
    text = ''
    for j in range(coset_size):
        for i in range(len(cosets)):
            text = text + cosets[i][j]
    return text

# computes the frequency table for a coset shefited to left with a given shift
def get_freq_dict(coset, shift):
    d = {}

    # TODO 1 compute the frequency of the letters in the coset shifted to left
    # by the shift parameter
    for letter in coset:
        shifted_letter = caesar_dec(letter, shift)
        d[shifted_letter] = d.get(shifted_letter, 0) + 1
	
    return d

# returns the shift computed for a coset
def find_correct_shift(coset):
    best_shift = 0
    min_distribution = math.inf

    for shift in range(26):
        shift_freq = get_freq_dict(coset, shift)
        distribution = compute_distribution(shift_freq)

        if min_distribution > distribution:
            min_distribution = distribution
            best_shift = shift
    
    return best_shift


def main():
    with open('msg_ex3.txt', 'r') as myfile:
        text = myfile.read().strip()

    dec_text = ''
    unmerged_cosets = []

    # TODO 3 decrypt the text
    cosets_list = split_in_cosets(text,7)

    for coset in cosets_list:
        unmerged_cosets.append(caesar_dec_string(coset,find_correct_shift(coset)))

    dec_text = merge_cosets(unmerged_cosets,len(unmerged_cosets[0]))

    print(dec_text)


if __name__ == "__main__":
    main()
