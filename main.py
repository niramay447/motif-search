from motif_search import *
from string_gen import *

strings,substrings = gen_str_and_substrings()

num_of_substrings=len(substrings[0])
matches = motifSearchUsingEditDist(substrings,num_of_substrings)
output_file = open("Out.txt", "w")

for i in matches:
    output_file.write(i+"\n")
output_file.close()
