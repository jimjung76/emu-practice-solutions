with open('cyclicnumbers.txt', 'r') as f:
    inputs = []
    for line in f:
        line = line.replace('\n', '')
        inputs.append(line)
    number = inputs[0]

outputs = []
for i in range(1, len(inputs)):
    true = 0
    for j in range(len(number)):
        if number[j] in str(int(number)*int(inputs[i])):
            true += 1

    if true == len(number):
        outputs.append('True')
    elif true < len(number):
        outputs.append('False')

for output in outputs:
    print(output)
