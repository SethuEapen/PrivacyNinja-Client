#Alexander Baran-Harper: https://www.youtube.com/watch?v=xfQlPWFlSgQ
import socket
import time
import RPi.GPIO as GPIO

host = '#ENTER SERVER IP ADDRESS HERE'
port = 5560 #YOU CAN CHANGE PORT IF THIS ONE IS USED UP

pir_sensor = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0

def setupSocket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    return s

def sendReceive(s, message):
    s.send(str.encode(message))
    reply = s.recv(1024)
    s.send(str.encode("EXIT"))
    s.close()
    reply = reply.decode('utf-8')
    return reply
def transmit(message):
    s = setupSocket()
    response = sendReceive(s, message)
    return response


try:
    while True:
        time.sleep(0.5)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            message = "DETECTED"
            print("Transmiting data")
            response = transmit(message)
            print(response)
            if response == 'KILL':
                break
            time.sleep(5)
            print("System Ready")
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()


