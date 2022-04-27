genedictionary = {}

acid_code = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I',
             'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V',
             'B', 'Z', 'X']
matrix = [
    [4, -1, -2, -2,  0, -1, -1,  0, -2, -1, -1, -
        1, -1, -2, -1,  1,  0, -3, -2,  0, -2, -1,  0],
    [-1,  5,  0, -2, -3,  1,  0, -2,  0, -3, -2,  2, -
        1, -3, -2, -1, -1, -3, -2, -3, -1,  0, -1],
    [-2,  0,  6,  1, -3,  0,  0,  0,  1, -3, -3,  0, -
        2, -3, -2,  1,  0, -4, -2, -3,  3,  0, -1],
    [-2, -2,  1,  6, -3,  0,  2, -1, -1, -3, -4, -
        1, -3, -3, -1,  0, -1, -4, -3, -3,  4,  1, -1],
    [0, -3, -3, -3,  9, -3, -4, -3, -3, -1, -1, -
        3, -1, -2, -3, -1, -1, -2, -2, -1, -3, -3, -2],
    [-1,  1,  0,  0, -3,  5,  2, -2,  0, -3, -2,  1,
        0, -3, -1,  0, -1, -2, -1, -2,  0,  3, -1],
    [-1,  0,  0,  2, -4,  2,  5, -2,  0, -3, -3,  1, -
        2, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1],
    [0, -2,  0, -1, -3, -2, -2,  6, -2, -4, -4, -
        2, -3, -3, -2,  0, -2, -2, -3, -3, -1, -2, -1],
    [-2,  0,  1, -1, -3,  0,  0, -2,  8, -3, -3, -
        1, -2, -1, -2, -1, -2, -2,  2, -3,  0,  0, -1],
    [-1, -3, -3, -3, -1, -3, -3, -4, -3,  4,  2, -3,
        1,  0, -3, -2, -1, -3, -1,  3, -3, -3, -1],
    [-1, -2, -3, -4, -1, -2, -3, -4, -3,  2,  4, -2,
        2,  0, -3, -2, -1, -2, -1,  1, -4, -3, -1],
    [-1,  2,  0, -1, -3,  1,  1, -2, -1, -3, -2,  5, -
        1, -3, -1,  0, -1, -3, -2, -2,  0,  1, -1],
    [-1, -1, -2, -3, -1,  0, -2, -3, -2,  1,  2, -1,
        5,  0, -2, -1, -1, -1, -1,  1, -3, -1, -1],
    [-2, -3, -3, -3, -2, -3, -3, -3, -1,  0,  0, -3,
        0,  6, -4, -2, -2,  1,  3, -1, -3, -3, -1],
    [-1, -2, -2, -1, -3, -1, -1, -2, -2, -3, -3, -
        1, -2, -4,  7, -1, -1, -4, -3, -2, -2, -1, -2],
    [1, -1,  1,  0, -1,  0,  0,  0, -1, -2, -2,  0, -
        1, -2, -1,  4,  1, -3, -2, -2,  0,  0,  0],
    [0, -1,  0, -1, -1, -1, -1, -2, -2, -1, -1, -
        1, -1, -2, -1,  1,  5, -2, -2,  0, -1, -1,  0],
    [-3, -3, -4, -4, -2, -2, -3, -2, -2, -3, -2, -
        3, -1,  1, -4, -3, -2, 11,  2, -3, -4, -3, -2],
    [-2, -2, -2, -3, -2, -1, -2, -3,  2, -1, -1, -
        2, -1,  3, -3, -2, -2,  2,  7, -1, -3, -2, -1],
    [0, -3, -3, -3, -1, -2, -2, -3, -3,  3,  1, -2,
        1, -1, -2, -2,  0, -3, -1,  4, -3, -2, -1],
    [-2, -1,  3,  4, -3,  0,  1, -1,  0, -3, -4,  0, -
        3, -3, -2,  0, -1, -4, -3, -3,  4,  1, -1],
    [-1,  0,  0,  1, -3,  3,  4, -2,  0, -3, -3,  1, -
        1, -3, -1,  0, -1, -3, -2, -2,  1,  4, -1],
    [0, -1, -1, -1, -2, -1, -1, -1, -1, -1, -1, -
        1, -1, -1, -2,  0,  0, -2, -1, -1, -1, -1, -1]
]

human = open("DLX5_human.fa")
for line in human:
    if not line.startswith(">"):
        genedictionary["human"] = line

mouse = open("DLX5_mouse.fa")
for line in mouse:
    if not line.startswith(">"):
        genedictionary["mouse"] = line

random = open("RandomSeq.fa")
for line in random:
    if not line.startswith(">"):
        genedictionary["random"] = line

human_mouse_ct = 0
for i in range(len(genedictionary["human"])):
    if genedictionary["human"][i] == genedictionary["mouse"][i]:
        human_mouse_ct = human_mouse_ct + 1

mouse_random_ct = 0
for i in range(len(genedictionary["mouse"])):
    if genedictionary["mouse"][i] == genedictionary["random"][i]:
        mouse_random_ct = mouse_random_ct + 1

random_human_ct = 0
for i in range(len(genedictionary["random"])):
    if genedictionary["random"][i] == genedictionary["human"][i]:
        random_human_ct = random_human_ct + 1


def BLOSUM_score(seq1, seq2):
    score = 0
    for i in range(len(seq1)):
        for j in range(len(acid_code)):
            if acid_code[j] == seq1[i]:
                x = j
                break
        for j in range(len(acid_code)):
            if acid_code[j] == seq2[i]:
                y = j
                break
        score = score + matrix[x][y]
    return score

#there is a "\n" at the end of the sequence line, so that we need to -1 for counting.
human_mouse_per = (human_mouse_ct-1)/(len(genedictionary["human"])-1)
mouse_random_per = (mouse_random_ct-1)/(len(genedictionary["mouse"])-1)
random_human_per = (random_human_ct-1)/(len(genedictionary["random"])-1)

print(human_mouse_ct-1, mouse_random_ct-1, random_human_ct-1)
print(human_mouse_per, mouse_random_per, random_human_per)
print(BLOSUM_score(genedictionary["human"], genedictionary["mouse"]), BLOSUM_score(
    genedictionary["mouse"], genedictionary["random"]), BLOSUM_score(genedictionary["random"], genedictionary["human"]))

