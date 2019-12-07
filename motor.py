import time
import board
import pulseio
from adafruit_motor import servo
from adafruit_motor import motor

# create a PWMOut object on Pin A2.
# duty_cycle=2 ** 15,
spd = pulseio.PWMOut(board.D13, frequency=0)

#   50 = clockwise
# < 50 = counterclockwise
dir = pulseio.PWMOut(board.D4, frequency=50)

# Create a servo object, my_servo.
#my_servo = servo.Servo(spd)
spd_servo = motor.DCMotor(spd, dir)
#dir_servo = servo.ContinuousServo(dir)

#while True:
#    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
#        my_servo.angle = angle
#        time.sleep(0.05)
#    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
#        my_servo.angle = angle
#        time.sleep(0.05)

spd_servo.throttle = 0.5
time.sleep(5.0)
spd_servo.throttle = 0
time.sleep(5.0)
spd_servo.throttle = -0.5
time.sleep(5.0)
spd_servo.throttle = 0
time.sleep(5.0)
