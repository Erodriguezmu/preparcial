import smtplib

message = 'Prueba'
subject = 'Prueba correo'

message = 'Subject: {}\n\n{}'.format(subject,message)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('sqlitebasedatos@gmail.com', 'parcial2021')

server.sendmail('sqlitebasedatos@gmail.com','paulavalentinabarrero@gmail.com', message)

server.quit()

print("Correo enviado con éxito")
