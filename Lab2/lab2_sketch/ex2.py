from caesar import *
import operator

# this is the list of bigrams, from most frequent to less frequent
bigrams = ["TH", "HE", 'IN', 'OR', 'HA', 'ET', 'AN',
           'EA', 'IS', 'OU', 'HI', 'ER', 'ST', 'RE', 'ND']

# this is the list of monograms, from most frequent to less frequent
monograms = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U',
             'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']

# this is the dictionary containing the substitution table (e.g. subst_table['A'] = 'B')
# TODO fill it in the create_subst_table function
subst_table = {}

# these are the dictionaries containing the frequency of the mono/bigrams in the text
# TODO fill them in the analize function
freq_table_bi = {}
freq_table_mono = {}

# sorts a dictionary d by the value


def sort_dictionary(d):
    sorted_dict = list(reversed(sorted(d.items(), key=operator.itemgetter(1))))
    return sorted_dict

# computes the frequencies of the monograms and bigrams in the text
def analize(text):
    global freq_table_bi

    # TODO 1.1 fill in the freq_table_mono dictionary
    for i in range(len(text) - 1):
        freq_table_mono[text[i]] = freq_table_mono.get( text[i], 0 ) + 1

    # TODO 1.2 fill in the freq_table_bi dictionary
    for i in range(len(text) - 1):
        freq_table_bi[text[i:i+2]] = freq_table_bi.get( text[i:i+2], 0 ) + 1

# creates a substitution table using the frequencies of the bigrams
def create_subst_table():
    global subst_table

    # TODO 2.1 sort the bigrams frequence table by the frequency
    sorted_freq_table_bi = sort_dictionary(freq_table_bi)

    # TODO 2.2 fill in the substitution table by associating the sorted frequence
    # dictionary with the given bigrams
    i = 0

    for bigram in sorted_freq_table_bi:
        if i >= len(bigrams):
            break
        
        subst_table[bigram[0][0]] = bigrams[i][0]
        subst_table[bigram[0][1]] = bigrams[i][1]
		
        i += 1    

# fills in the letters missing from the substitution table using the frequencies
# of the monograms


def complete_subst_table():
    global subst_table

    # TODO 3.1 sort the monograms frequence table by the frequency
    sorted_freq_table_mono = sort_dictionary(freq_table_mono)

    # TODO 3.2 fill in the missing letters from the substitution table by
    # associating the sorted frequence dictionary with the given monograms
    i = 0
    for mono in sorted_freq_table_mono:
        if mono[0] not in subst_table:
            subst_table[mono[0]] = monograms[i]

        i += 1

# this is magic stuff used in main


def adjust():
    global subst_table
    subst_table['Y'] = 'B'
    subst_table['E'] = 'L'
    subst_table['L'] = 'M'
    subst_table['P'] = 'W'
    subst_table['F'] = 'C'
    subst_table['X'] = 'F'
    subst_table['J'] = 'G'
    subst_table['I'] = 'Y'


def decrypt_text(text):
    global subst_table

    # TODO 4 decrypt and print the text using the substitution table
    plaintext = ""
    
    for c in text:
    	if c in subst_table:
    		plaintext += subst_table[c]

    return plaintext

def main():
    with open('msg_ex2.txt', 'r') as myfile:
        text = myfile.read()

    analize(text)
    create_subst_table()
    complete_subst_table()
    adjust()
    print(decrypt_text(text))

if __name__ == "__main__":
    main()
