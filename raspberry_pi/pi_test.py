import RPi.GPIO as GPIO
import time

# Set the pin numbering mode to BCM
GPIO.setmode(GPIO.BCM)

# Define the pins for the LEDs
led_pins = [18, 23, 24]

# Set up the GPIO pins for the LEDs
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)

# Loop through the LEDs and turn them on and off in sequence
while True:
    for pin in led_pins:
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin, GPIO.LOW)
