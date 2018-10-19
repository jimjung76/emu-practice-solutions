import numpy as np

def piratetreasure(file):
    outputforeachline = []
    with open(file, 'r') as f:
        for line in f:
            totalcoins, pirates = line.split()
            totalcoins, pirates = int(totalcoins), int(pirates)

            coinsforeachpirate = []

            for i in range(pirates):
                coinstaken = int(np.ceil(totalcoins/pirates))
                coinsremaining = totalcoins - int(np.ceil(totalcoins/pirates))
                totalcoins = coinsremaining

                coinsforeachpirate.append(str(coinstaken))
            coinsforeachpirate.append(str(coinsremaining))

            outputforeachline.append(coinsforeachpirate)

    return outputforeachline

outputforeachline = piratetreasure('piratetreasureinputfile.txt')
for i in range(len(outputforeachline)):
    output = ' '.join(outputforeachline[i])
    print(output)
