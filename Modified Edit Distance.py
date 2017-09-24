# Cost of character substitutions
SUBSTITUTION_TABLE = [
    [0, 5, 3, 2, 3, 3, 4, 5, 8, 6, 7, 8, 7, 6, 8, 9, 1, 3, 1, 4, 6, 4, 1, 2, 6, 1],
    [5, 0, 2, 3, 4, 3, 1, 1, 4, 3, 4, 5, 2, 1, 4, 5, 6, 3, 3, 3, 2, 1, 5, 3, 2, 4],
    [3, 2, 0, 1, 2, 1, 2, 3, 5, 4, 6, 7, 4, 3, 6, 7, 3, 2, 1, 2, 4, 1, 2, 1, 2, 2],
    [2, 3, 1, 0, 1, 1, 2, 3, 5, 4, 5, 6, 5, 4, 6, 7, 3, 1, 1, 2, 4, 2, 2, 1, 3, 2],
    [3, 4, 2, 1, 0, 1, 2, 3, 5, 4, 5, 6, 5, 4, 6, 7, 2, 1, 1, 2, 4, 2, 1, 2, 3, 2],
    [3, 3, 1, 1, 1, 0, 1, 2, 4, 3, 4, 5, 4, 3, 4, 6, 3, 1, 2, 1, 3, 1, 2, 2, 2, 3],
    [4, 1, 2, 2, 2, 1, 0, 1, 3, 2, 3, 4, 3, 2, 4, 5, 5, 2, 3, 1, 2, 1, 4, 3, 1, 4],
    [5, 1, 3, 3, 3, 2, 1, 0, 2, 1, 2, 3, 2, 1, 3, 4, 6, 3, 4, 2, 1, 2, 5, 4, 1, 5],
    [8, 4, 5, 5, 5, 4, 3, 2, 0, 1, 1, 2, 2, 2, 1, 2, 7, 4, 6, 3, 1, 5, 6, 6, 2, 7],
    [6, 3, 4, 4, 4, 3, 2, 1, 1, 0, 1, 2, 1, 1, 2, 3, 7, 4, 5, 3, 1, 3, 6, 5, 2, 6],
    [7, 4, 6, 5, 5, 4, 3, 2, 1, 1, 0, 1, 1, 2, 1, 2, 8, 5, 6, 4, 2, 4, 7, 6, 3, 7],
    [8, 5, 7, 6, 6, 5, 4, 3, 2, 2, 1, 0, 2, 3, 1, 1, 9, 6, 7, 5, 3, 5, 8, 7, 4, 8],
    [7, 2, 4, 5, 5, 4, 3, 2, 2, 1, 1, 2, 0, 1, 2, 3, 8, 5, 6, 4, 2, 3, 7, 5, 3, 6],
    [6, 1, 3, 4, 4, 3, 2, 1, 2, 1, 2, 3, 1, 0, 3, 4, 7, 4, 5, 3, 2, 2, 6, 4, 2, 5],
    [8, 4, 6, 6, 6, 4, 4, 3, 1, 2, 1, 1, 2, 3, 0, 1, 8, 5, 7, 4, 2, 5, 7, 7, 3, 8],
    [9, 5, 7, 7, 7, 6, 5, 4, 2, 3, 2, 1, 3, 4, 1, 0, 9, 6, 8, 5, 4, 5, 8, 7, 4, 8],
    [1, 6, 3, 3, 2, 3, 5, 6, 7, 7, 8, 9, 8, 7, 8, 9, 0, 3, 1, 4, 6, 4, 1, 3, 5, 2],
    [3, 3, 2, 1, 1, 1, 2, 3, 4, 4, 5, 6, 5, 4, 5, 6, 3, 0, 2, 1, 3, 2, 2, 2, 2, 3],
    [1, 3, 1, 1, 1, 2, 3, 4, 6, 5, 6, 7, 6, 5, 7, 8, 1, 2, 0, 3, 5, 3, 1, 1, 4, 1],
    [4, 3, 2, 2, 2, 1, 1, 2, 3, 3, 4, 5, 4, 3, 4, 5, 4, 1, 3, 0, 2, 2, 3, 3, 1, 5],
    [6, 2, 4, 4, 4, 3, 2, 1, 1, 1, 2, 3, 2, 2, 2, 4, 6, 3, 5, 2, 0, 4, 5, 3, 1, 6],
    [4, 1, 1, 2, 2, 1, 1, 2, 5, 3, 4, 5, 3, 2, 5, 5, 4, 2, 3, 2, 4, 0, 5, 2, 2, 3],
    [1, 5, 2, 2, 1, 2, 4, 5, 6, 6, 7, 8, 7, 6, 7, 8, 1, 2, 1, 3, 5, 5, 0, 2, 4, 2],
    [2, 3, 1, 1, 2, 2, 3, 4, 6, 5, 6, 7, 5, 4, 7, 7, 3, 2, 1, 3, 3, 2, 2, 0, 4, 1],
    [6, 2, 2, 3, 3, 2, 1, 1, 2, 2, 3, 4, 3, 2, 3, 4, 5, 2, 4, 1, 1, 2, 4, 4, 0, 4],
    [1, 4, 2, 2, 2, 3, 4, 5, 7, 6, 7, 8, 6, 5, 8, 8, 2, 3, 1, 5, 6, 3, 2, 1, 4, 0],
]

with open('wordlist.txt', 'r') as file:
    WORDS = file.readlines()

WORDS = [x.strip() for x in WORDS]
WORDS = [x for x in WORDS if x.isalpha()]

def ModifiedLevenshteinDistance(s, t):
    # for all i and j, d[i, j] will hold the Levenshtein distance between
    # the first i characters of s and the first j characters of t
    # note that d has(m + 1) * (n + 1) values
    dp = [[0 for x in range(len(t) + 1)] for y in range(len(s) + 1)]

    # source prefixes can be transformed into empty string by
    # dropping all characters
    for i in range(1, len(s) + 1):
        dp[i][0] = i

    # target prefixes can be reached from empty source prefix
    # by inserting every character
    for j in range(1, len(t) + 1):
        dp[0][j] = j

    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            substitutionCost = SUBSTITUTION_TABLE[ord(s[i - 1]) - ord('a')][ord(t[j - 1]) - ord('a')]
            dp[i][j] = min(dp[i - 1][j] + 1,  # deletion
                       dp[i][j - 1] + 1,  # insertion
                       dp[i - 1][j - 1] + substitutionCost)  # substitution
    # print(dp)
    return dp[len(s)][len(t)]

#a = input()
#b = input()
#print(ModifiedLevenshteinDistance(a, b))

query = input()
bestmatch = []

for word in WORDS:
    bestmatch.append((ModifiedLevenshteinDistance(query, word), word))

bestmatch.sort()

for i in range(10):
    print(bestmatch[i])
