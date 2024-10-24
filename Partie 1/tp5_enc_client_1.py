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

msg = str(FirstNB)+Operator+str(SecondNB)
EncodedMessage = msg.encode('utf-8')
msg_len = len(EncodedMessage)
header = msg_len.to_bytes(4, byteorder='big')
payload = header + EncodedMessage + ("<truc>").encode('utf-8')
print("Tentative d'envoie de message : "+str(payload))
s.send(payload)
print("Message envoyé !")
s.close()



# LenData = str(len(str(FirstNB)+Operator+str(SecondNB)))
# LenData4Bit = "0"* (4 - len(LenData) )+ LenData
# print("bit : "+LenData4Bit)



# match Operator :
#     case "+":
#         Result = FirstNB+SecondNB
#     case "-":
#         Result = FirstNB-SecondNB
#     case "/":
#         Result = FirstNB/SecondNB
#     case "*":
#         Result = FirstNB*SecondNB
#     case _ :
#         print("Opérateur inconnu : "+Operator)
#         exit(1)
# print(Result)



# s.send(UserInput.encode())

# data = s.recv(1024)
# s.close()
# print(data.decode())
# s.close()
