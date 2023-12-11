#import RPi.GPIO as GPIO 
#import time
#import smtplib 

#GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#def read_gas_sensor():
#    return GPIO.input(2)

#def send_gas_alert():
#    gas_level = read_gas_sensor()
#    if gas_level == 1:
#        message = "¡Alerta de gas!"
#        send_email(message)

# Función para enviar un correo electrónico
#def send_email(message):
    # Configuración del servidor de correo electrónico
#    server = smtplib.SMTP("smtp.gmail.com", 587)
#    server.ehlo()
#    server.starttls()
#    server.login("your_email@gmail.com", "your_password")
    
    # Envío del correo electrónico
#    subject = "Alarma de seguridad"
#    body = message
#    server.sendmail("your_email@gmail.com", "your_email@gmail.com", "Subject: " + subject + "\n\n" + body)
#    server.close()
