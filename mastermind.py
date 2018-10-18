def mastermind(code, guess):
    newCode = str(code)
    newGuess = str(guess)
    black = 0
    white = 0

    for i in range(4):
        if newCode[i] == newGuess[i]:
            black += 1
        elif newGuess[i] in newCode:
            white += 1
    print("%d %d"%(black, white))


