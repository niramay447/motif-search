# calculating edit distance between two strings
def get_edit_distance(string1, string2):
    length1 = len(string1)
    length2 = len(string2)

    arr = [[0 for _ in range(length1 + 1)] for _ in range(2)]
    for i in range(0, length1 + 1):
        arr[0][i] = i
    for i in range(1, length2 + 1):
        for j in range(0, length1 + 1):
            if (j == 0):
                arr[i % 2][j] = i

            elif (string1[j - 1] == string2[i - 1]):
                arr[i % 2][j] = arr[(i - 1) % 2][j - 1]
            else:
                mini = min(arr[i % 2][j - 1],arr[(i - 1) % 2][j - 1])
                arr[i % 2][j] = (1 + min(arr[(i - 1) % 2][j],mini))

    return arr[length2 % 2][length1]

