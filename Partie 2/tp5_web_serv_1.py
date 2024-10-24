import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.33.77.14', 13337 ))  

s.listen(1)
conn, addr = s.accept()

while True :
    try :
        data = conn.recv(1024)
        if not data :break
        print(data)
        url = str(data).split(" ")[1]
        if url == "/":
            toSend = 'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello je suis un serveur HTTP</h1>\r\n'
            conn.send(toSend.encode())
        else :
            toSend = 'HTTP/1.0 404 ERROR\r\nContent-Type: text/html\r\n\r\n<h1>Erreur 404 ou quoi la , jsp ce que tu fout la</h1>\r\n'
            conn.send(toSend.encode())
        break
    except socket.error:
        print("Error Occured.")
        break
conn.close()