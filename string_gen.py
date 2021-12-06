# generating 20 random strings of 600 characters

import random
from itertools import combinations

SIZE=600
ALPHABET_SET = ["A", "C", "G", "T"]
SUBSTRING_LEN=15
NUM = 20
def gen_str_and_substrings():
    strings = []
    substrings = []
    input_file = open("inputs.txt", "w")
    for i in range(NUM):
        random_string = ''.join(random.choices(ALPHABET_SET, k = SIZE))
        strings.append(random_string)
        substring = [random_string[x:y] for x, y in combinations(range(len(random_string) + 1), r=2) if len(random_string[x:y]) == SUBSTRING_LEN]

        input_file.write(random_string + "\n")
        substrings.append(substring)
    input_file.close()

    return strings, substrings