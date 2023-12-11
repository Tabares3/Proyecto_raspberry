#import RPi.GPIO as GPIO
#import time
#import smtplib

#GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#def read_room_sensor():
#    return GPIO.input(6)

#def send_room_alert():
#    room_status = read_room_sensor()
#    if room_status == 1:
#        message = "¡Alerta en la habitación!"
#        send_email(message)
