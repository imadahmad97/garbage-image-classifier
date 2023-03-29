import RPi.GPIO as GPIO
import time



GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)



servo.start(0)
print("Waiting for 1 second")
time.sleep(1)

print("Rotating from 0 to 90 degrees")
duty = 2
while duty <= 7:
    servo.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty = duty + 1

print("Waiting for 1 second")
time.sleep(7)

print("Rotating from 90 to 0 degrees")
duty = 7
while duty >= 2:
    servo.ChangeDutyCycle(duty)
    time.sleep(0.05)
    duty = duty - 1

print("Turning back to 0 degrees")
servo.ChangeDutyCycle(0)
time.sleep(1)
servo.stop()
GPIO.cleanup()
print("Done and Dusted")
