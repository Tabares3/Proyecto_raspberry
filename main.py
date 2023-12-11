print("hola juan")

# se toca que comentar ya que este es el codigo de pi3_del proyecto_raspberry
# import RPi.GPIO as GPIO
#import smtplib

# Define los pines GPIO 
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(17, GPIO.OUT)
#GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define las variables globales
#sensor_status = [0, 0, 0, 0, 0]
#alarm_enabled = False

# Función para inicializar el sistema
#def init():
#    global sensor_status
#    global alarm_enabled
#    sensor_status = [GPIO.input(2), GPIO.input(3), GPIO.input(4), GPIO.input(5), GPIO.input(6)]
#    alarm_enabled = GPIO.input(26)

# Función para obtener el estado de los sensores
#def get_sensor_status():
#    global sensor_status
#    return sensor_status

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

# Función para activar la alarma
#def activate_alarm():
#    global alarm_enabled
#    alarm_enabled = True

# Función para desactivar la alarma
#def deactivate_alarm():
#    global alarm_enabled
#    alarm_enabled = False

# Bucle principal
#while True:
    # Actualiza el estado de los sensores
#    sensor_status = [GPIO.input(2), GPIO.input(3), GPIO.input(4), GPIO.input(5), GPIO.input(6)]

    # Verifica si se activó algún sensor
#    for i in range(len(sensor_status)):
#        if sensor_status[i] == 1 and alarm_enabled:
#            # Envía un correo electrónico de alarma
#            send_email("Sensor " + str(i + 1) + " activado")
#            GPIO.output(17, GPIO.HIGH)
#            time.sleep(1)
#            GPIO.output(17, GPIO.LOW)

# Verifica si se activó el interruptor de alarma
#    if GPIO.input(26) == 0:
#        # Si se activó, activa o desactiva la alarma
#        if alarm_enabled:
#            deactivate_alarm()
#        else:
#            activate_alarm()(""") 