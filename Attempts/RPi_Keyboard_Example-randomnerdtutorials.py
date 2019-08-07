#https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/
#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
pir_sensor = 11
NULL_CHAR = chr(0)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pir_sensor, GPIO.IN)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

time.sleep(5)
print("Initialization over. System armed")
current_state = 0
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
            write_report(chr(5)+NULL_CHAR+chr(26)+NULL_CHAR*5)
            write_report(NULL_CHAR*8)
            time.sleep(5)
            #break IF YOU WANT TO CLOSE AFTER ONE USE
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
