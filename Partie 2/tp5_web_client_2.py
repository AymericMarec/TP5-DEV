import socket

host = '10.33.77.14'
port = 13337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

payload = "GET /shrek \r\n"
s.send(payload.encode())
print("Message envoyé !")
tailleImage = s.recv(8)
tailleImage = int(tailleImage.decode())
contenuTelecharge = 0
fichierImage = open("image.jpg","wb")

while contenuTelecharge < tailleImage:
    contenuRecu = s.recv(1024)
    fichierImage.write(contenuRecu)
    contenuTelecharge += len(contenuRecu)
fichierImage.close()

print("Shrek téléchargé")
s.close()