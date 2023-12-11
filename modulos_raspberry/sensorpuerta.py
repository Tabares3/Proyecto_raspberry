#import RPi.GPIO as GPIO
#import time
#import smtplib

#GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#def is_door_open():
#    return GPIO.input(3)

#def send_door_alert():
#    if is_door_open() == 1:
#        message = "¡Alerta de puerta abierta!"
#        send_email(message)
