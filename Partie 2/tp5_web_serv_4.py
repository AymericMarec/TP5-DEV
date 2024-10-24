import socket
import time
import datetime
import os

def FormatLog(message,type):
    ts = time.time()
    sent = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') +" "+ type +" "+ message
    return sent

def AddLog(log):
    logFile = open(LOG_PATH, "a")
    print(log)
    logFile.write(log)
    logFile.close()

pathFolder = os.path.join(os.getenv('localappdata'), "Temp", "web")
global LOG_PATH
LOG_PATH = os.path.join(os.getenv('localappdata'), "Temp", "web","web.log")
if not(os.path.exists(pathFolder) and os.path.isdir(pathFolder)):
    os.makedirs(pathFolder)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('10.33.77.14', 13337 ))  

s.listen(1)
conn, addr = s.accept()

while True :
    try :
        data = conn.recv(1024)
        if not data :break
        url = str(data).split(" ")[1]
        if url == "/":
            toSend = 'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>Hello je suis un serveur HTTP</h1>\r\n'
            AddLog(FormatLog("Un utilisateur est venu sur le site sur l'url /","INFO"))
            conn.send(toSend.encode())
        elif url == "/index":
            file = open('./view/index.html')
            html_content = file.read()
            file.close()
            print("fichier lu ")
            toSend = f'HTTP/1.0 200 OK\r\nContent-Type: text/html\r\n\r\n{html_content}\r\n'
            conn.send(toSend.encode())
            AddLog(FormatLog("Un utilisateur a téléchargé l'index.html","INFO"))

        else :
            toSend = 'HTTP/1.0 404 ERROR\r\nContent-Type: text/html\r\n\r\n<h1>Erreur 404 ou quoi la , jsp ce que tu fout la</h1>\r\n'
            conn.send(toSend.encode())
            AddLog(FormatLog("Un utilisateur s'est perdu la , il est sur une 404","INFO"))

        break
    except socket.error:
        print("Error Occured.")
        break
conn.close()