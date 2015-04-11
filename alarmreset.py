import time
import RPi.GPIO as io
io.setmode(io.BCM)


RED_LED_1 = 24
RED_LED_2 = 25


io.setup(RED_LED_1, io.OUT)
io.setup(RED_LED_2, io.OUT)

while True:
	io.output(RED_LED_1, False);
	io.output(RED_LED_2, False);

GPIO.cleanup()
