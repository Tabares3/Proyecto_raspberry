import time
import smtplib

# Configuración del servidor de correo electrónico
tu_servidor_smtp = "tu_servidor_smtp"
tu_puerto_smtp = 587  # Sustituye con el puerto SMTP que estás utilizando
tu_email = "tu_email@gmail.com"
tu_contraseña = "tu_contraseña"

def read_gas_sensor():
    # Lógica para leer el sensor de gas (simulado)
    gas_level = 0  # Simula la lectura del sensor de gas
    return gas_level

def send_gas_alert():
    gas_level = read_gas_sensor()
    if gas_level > 0:
        message = f"¡Alerta de gas! Nivel de gas: {gas_level}"
        send_email(message)

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

# Bucle principal del sensor de gas (simulado)
while True:
    send_gas_alert()
    time.sleep(1)  # Simula el tiempo entre iteraciones
