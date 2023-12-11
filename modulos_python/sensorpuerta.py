import time
import smtplib

import time
import smtplib

# Configuración del servidor de correo electrónico
tu_servidor_smtp = "tu_servidor_smtp"
tu_puerto_smtp = 587  # Reemplaza con el puerto SMTP que estás utilizando
tu_email = "tu_email@gmail.com"
tu_contraseña = "tu_contraseña"

def is_door_open():
    # Lógica para verificar si la puerta está abierta (simulado)
    return False  # Simula la lectura del estado de la puerta

def send_email(message):
    # Configuración del servidor de correo electrónico
    server = smtplib.SMTP(tu_servidor_smtp, tu_puerto_smtp)
    server.ehlo()
    server.starttls()
    server.login(tu_email, tu_contraseña)

    # Envío del correo electrónico
    subject = "Alarma de seguridad"
    body = message
    server.sendmail(tu_email, tu_email, "Subject: " + subject + "\n\n" + body)
    server.close()

def send_door_alert():
    if is_door_open():
        message = "¡Alerta de puerta abierta!"
        send_email(message)

# Bucle principal del sensor de puerta (simulado)
while True:
    send_door_alert()
    time.sleep(1)  # Simula el tiempo entre iteraciones

