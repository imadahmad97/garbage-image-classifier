import RPi.GPIO as GPIO
import time
import picamera
import io
import tensorflow as tf
import numpy as np

# Loading in model
model = tf.keras.models.load_model('./assets/CNN_3Class_Best.h5')

# Getting image with camera
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    
    input_image_buffer = io.BytesIO()
    camera.capture(input_image_buffer, 'jpeg')
    
    input_image_buffer.seek(0)
    input_image = input_image_buffer.read()

prediction = np.argmax(model.predict(np.expand_dims(input_image)).reshape(-1)

# Compost motor
if prediction == 0:
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(11,GPIO.OUT)
    servo = GPIO.PWM(11,50)



    servo.start(0)

    time.sleep(1)


    duty = 2
    while duty <= 7:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.05)
        duty = duty + 1


    time.sleep(7)


    duty = 7
    while duty >= 2:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.05)
        duty = duty - 1


    servo.ChangeDutyCycle(0)
    time.sleep(1)
    servo.stop()
    GPIO.cleanup()

# Recycling motor
elif prediction == 1:
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(13,GPIO.OUT)
    servo = GPIO.PWM(13,50)



    servo.start(0)

    time.sleep(1)


    duty = 2
    while duty <= 7:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.05)
        duty = duty + 1


    time.sleep(7)


    duty = 7
    while duty >= 2:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.05)
        duty = duty - 1


    servo.ChangeDutyCycle(0)
    time.sleep(1)
    servo.stop()
    GPIO.cleanup()

# Trash motor
else:
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(15,GPIO.OUT)
    servo = GPIO.PWM(15,50)



    servo.start(0)

    time.sleep(1)


    duty = 2
    while duty <= 7:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.05)
        duty = duty + 1


    time.sleep(7)


    duty = 7
    while duty >= 2:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.05)
        duty = duty - 1


    servo.ChangeDutyCycle(0)
    time.sleep(1)
    servo.stop()
    GPIO.cleanup()
