def blackandwhite():
    black, white = 0, 0
    for j in range(4):
        if guess[j] == code[j]:
            black += 1
        elif guess[j] in code:
            white += 1
    print(str(black) + ' ' + str(white))

with open('mastermind.txt', 'r') as f:
    content = f.read().split('\n')
for i in range(len(content)):
    if content[i] == '':
        code = content[i-2]
        guess = content[i-1]
        blackandwhite()
    elif i == (len(content) - 2):
        code = content[i]
        guess = content[i+1]
        blackandwhite()
