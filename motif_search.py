# motif search using minimum edit distance
from string_gen import *
from edit_dist import *
matches = []

def motifSearchUsingEditDist(substrings,num_of_substrings):
    for i in range(NUM):
        for j in range(num_of_substrings):
            count = 0
            flag = False
            for k in range(NUM):
                if i == k:
                    same_row=True
                    continue
                for l in range(num_of_substrings):
                    dis = min_edit_dist(substrings[i][j],substrings[k][l],1,1)
                    if dis<=5:
                        flag = True
                        break
                if flag==True:
                    count+=1
                else:
                    break
            match = substrings[i][j]
            if count==19:
                matches.append(match)
            if same_row==True or flag==True:
                break
    return matches