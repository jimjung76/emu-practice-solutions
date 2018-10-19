import numpy as np

with open('wordsquare.txt', 'r') as f:
    words = []
    for line in f:
        line = line.replace('\n', '')
        letters = list(line)
        words.append(letters)
    wordarray = np.array(words)

for i in range(len(wordarray[0])):
    wordarray[0] = wordarray[i]
    wordarray[i] = wordarray[0]
    for j in range(len(wordarray[0])):
        wordarray[i][j]
