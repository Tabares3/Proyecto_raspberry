import time
import smtplib

# Definición de las variables de configuración
tu_servidor_smtp = "tu_servidor_smtp"
tu_puerto_smtp = 587  # Reemplaza con el puerto SMTP que estás utilizando
tu_email = "tu_email@gmail.com"
tu_contraseña = "tu_contraseña"

def read_bedroom_sensor():
    # Lógica para leer el sensor de la habitación (simulado)
    bedroom_status = 0  # Simula la lectura del sensor de la habitación
    return bedroom_status

def send_email(message):
    # Configuración del servidor de correo electrónico
    server = smtplib.SMTP(tu_servidor_smtp, tu_puerto_smtp)
    server.ehlo()
    server.starttls()
    server.login(tu_email, tu_contraseña)

    # Envío del correo electrónico
    subject = "Alarma en la habitación"
    body = message
    server.sendmail(tu_email, tu_email, "Subject: " + subject + "\n\n" + body)
    server.close()

def send_bedroom_alert():
    bedroom_status = read_bedroom_sensor()
    if bedroom_status > 0:
        message = f"¡Alerta en la habitación! Estado: {bedroom_status}"
        send_email(message)

# Bucle principal del sensor de la habitación (simulado)
while True:
    send_bedroom_alert()
    time.sleep(1)  # Simula el tiempo entre iteraciones
