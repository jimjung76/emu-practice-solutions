def cyclicNum(init,a,b,c,d,e):
    strInit = str(init)
    a = str(a*init)
    b = str(b*init)
    c = str(c*init)
    d = str(d*init)
    e = str(e*init)
    counter = 0
    list = [a,b,c,d,e]
    for c in range(len(list)):
        for i in range(len(strInit)):
            if strInit[i] in list[c]:
                counter += 1

        if counter == len(strInit):
            print(True)
        else:
            print(False)
        counter = 0

"""
example run; cyclicNum(142857,6,2,7,5,12)
True
True
False
True
False
"""

