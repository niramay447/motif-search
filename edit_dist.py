# calculating edit distance between two strings
# def get_edit_distance(string1, string2):
#     length1 = len(string1)
#     length2 = len(string2)
#
#     arr = [[0 for _ in range(length1 + 1)] for _ in range(2)]
#     for i in range(0, length1 + 1):
#         arr[0][i] = i
#     for i in range(1, length2 + 1):
#         for j in range(0, length1 + 1):
#             if (j == 0):
#                 arr[i % 2][j] = i
#
#             elif (string1[j - 1] == string2[i - 1]):
#                 arr[i % 2][j] = arr[(i - 1) % 2][j - 1]
#             else:
#                 mini = min(arr[i % 2][j - 1],arr[(i - 1) % 2][j - 1])
#                 arr[i % 2][j] = (1 + min(arr[(i - 1) % 2][j],mini))
#
#     return arr[length2 % 2][length1]


# Below are the costs of different operations.
def min_edit_dist(string1,string2,indel,sub):
    len1=len(string1)
    len2=len(string2)

    matr = [[0 for i in range(len2+1)] for j in range(len1+1)]
    for i in range(len1+1):
        for j in range(len2+1):
            if i==0:
                matr[i][j]=j*indel
            elif j==0:
                matr[i][j]==i*indel
            elif string1[i-1]==string2[j-1]:
                matr[i][j]=matr[i-1][j-1]

            else:
                matr[i][j] = min(matr[i - 1][j - 1] + sub,
                    min(matr[i - 1][j] + indel, matr[i][j - 1] + indel))

    return matr[len1][len2]
