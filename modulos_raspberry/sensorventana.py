#import RPi.GPIO as GPIO
#import time
#import smtplib

#GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#def is_window_open():
#    return GPIO.input(5)

#def send_window_alert():
#    if is_window_open() == 1:
#        message = "¡Alerta de ventana abierta!"
#        send_email(message)
