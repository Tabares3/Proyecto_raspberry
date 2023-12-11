#import RPi.GPIO as GPIO
#import time
#import smtplib

#GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#def is_fire_detected():
#    return GPIO.input(4)

#def send_fire_alert():
#    if is_fire_detected() == 1:
#        message = "¡Alerta de incendio detectado!"
#        send_email(message)
