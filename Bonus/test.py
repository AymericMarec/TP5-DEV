def CalculTailleBit(Nb):
    bit = 0
    while True:
        bit+=1
        if Nb < 2**bit :
            return bit
# print(CalculTailleBit(5)) 