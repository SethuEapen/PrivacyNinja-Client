#Pi My Life Up: https://www.youtube.com/watch?v=mmS7EsI0Sao
import RPi.GPIO as GPIO
import time

pir_sensor = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0
try:
    while True:
        time.sleep(0.5)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
