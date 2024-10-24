import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.33.77.14', 13337 ))  

s.listen(1)
conn, addr = s.accept()

while True:

    try:
        header = conn.recv(1)
        if not header: break
        msglen = int.from_bytes(header[0:4], byteorder='big')
        print(f"Lecture des {msglen} prochains octets")
        message = conn.recv(msglen)
        end = conn.recv(6)
        message = message.decode('utf-8')
        end = end.decode('utf-8')
        print(msglen,message,end)
            
    except socket.error:
        print("Error Occured.")
        break

conn.close()
