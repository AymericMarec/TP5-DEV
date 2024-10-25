import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.33.77.14', 13337 ))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        infos = conn.recv(2)
        if not infos: break
        infosINT = int.from_bytes(infos, byteorder='big')
        infosBIN = bin(infosINT)[2:]
        print(infos)
        print(infosINT)
        print(infosBIN)
        # nb2 = conn.recv(3)
        # if not nb2:break
        # msg_bin1 = bin(int.from_bytes(infos_nb1, byteorder='big'))[2:].zfill(24)
        # msg_bin2 = bin(int.from_bytes(nb2, byteorder='big'))[2:].zfill(24)
        # operator_bin = msg_bin1[0:2]
        # nb1_signe_bin = msg_bin1[2:3]
        # nb2_signe_bin = msg_bin1[3:4]
        # nb1 = int(msg_bin1[5:],2)
        # nb2 = int(msg_bin2,2)
        # match int(operator_bin,2) :
        #     case 0:
        #         operator = "+"
        #     case 1:
        #         operator = "-"
        #     case 2:
        #         operator = "/"
        #     case 3:
        #         operator = "*"
        # if nb1_signe_bin == bin(0) :
        #     nb1*-1
        # if nb2_signe_bin == bin(0) :
        #     nb2*-1
        # calcul = str(nb1) + operator + str(nb2)
        # result = eval(calcul)
        # print(result)
        
    except socket.error:
        print("Error Occured.")
        break
conn.close()