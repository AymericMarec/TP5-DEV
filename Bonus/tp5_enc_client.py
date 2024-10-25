import socket
import re

def GetFirstNB(UserInput):
    index = 1
    while True:
        try:
            int(UserInput[0:index])
            index+=1
        except:
            if index == 1:
                index+=1
                continue
            return int(UserInput[0:index-1]),index

def CalculTailleBit(Nb):
    bit = 0
    while True:
        bit+=1
        if Nb < 2**bit :
            return bit


host = '10.33.77.14'
port = 13337 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))      
        
UserInput = input("Entrez une opération ( nombre + opérateur + nombre), avec des nombres compris entre -100000 et 100000\n\nExemple :\n\n3 + 2\n5*6\n\n\n")
if not(re.search("^-{0,1}\d+\s*[+\-*\/]\s*-{0,1}\d+$",UserInput)):
    print("Mauvais Format d'entrée")
    exit(0)

UserInput = UserInput.replace(" ", "")
FirstNB , index = GetFirstNB(UserInput)
Operator = UserInput[index-1]
SecondNB = int(UserInput[index:len(UserInput)])
if(FirstNB <= -1048575 or FirstNB >= 1048575 or SecondNB <= -1048575 or SecondNB >= 1048575):
    print("Nombre trop grand")
    exit(2)

FirstPositive = 1
SecondPositive = 1
if(FirstNB < 0):
    FirstPositive = 0
    FirstNB *= -1 
if(SecondNB < 0):
    SecondPositive = 0
    SecondNB *= -1 

match Operator :
    case "+":
        OpertorBin = 0
    case "-":
        OpertorBin = 1
    case "/":
        OpertorBin = 2
    case "*":
        OpertorBin = 3
    case _ :
        print("Opérateur inconnu : "+Operator)
        exit(1)

FirstNBByte = str(FirstNB).encode()
SecondNBByte = str(SecondNB).encode()
# OperatorShift = OpertorBin << 22


BitAvailable = 6
OctetToSend = 2
BitToGet = CalculTailleBit(FirstNB)+CalculTailleBit(SecondNB)
while True :
    if BitToGet >= BitAvailable :
        BitAvailable+=8
        OctetToSend+=1
    else :
        break
print(OctetToSend) 
print(BitAvailable)

Nb1SigneShift = FirstPositive << 2
Nb2SigneShift = SecondPositive << 3
TailleNb1Shift = CalculTailleBit(FirstNB) << 4
TailleNb2Shift = CalculTailleBit(SecondNB) << 7
if(CalculTailleBit(FirstNB)%3 == 1):
    Toadd = CalculTailleBit(FirstNB) +2
elif(CalculTailleBit(FirstNB)%3 == 2):
    Toadd = CalculTailleBit(FirstNB) +1
else :
    Toadd = CalculTailleBit(FirstNB)
Nb1Shift = FirstNB << 10
Nb2Shift = SecondNB << 10 + Toadd
infos = OpertorBin | Nb1SigneShift | Nb2SigneShift  | TailleNb1Shift | TailleNb2Shift | Nb1Shift | Nb2Shift
print("infos : ",infos)
print(CalculTailleBit(infos))
print(infos.to_bytes(CalculTailleBit(infos),byteorder='big'))
s.send(infos.to_bytes(OctetToSend,byteorder='big'))


# Octet_1 = OpertorBin | Nb1SigneShift | Nb2SigneShift | int(FirstNBByte)
# print(Octet_1)
# Octet_2 = int(SecondNBByte)

# payload = Octet_1.to_bytes(3,byteorder='big') + Octet_2.to_bytes(3,byteorder='big')
# s.send(payload)
print("Message envoyé !")
s.close()