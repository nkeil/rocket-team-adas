
import os
import board
import digitalio
import time
import busio
import adafruit_bno055

#modules to access SD card and filesystem
import adafruit_sdcard
import storage
from digitalio import DigitalInOut, Direction

#needed for the motor
import pulseio
from adafruit_motor import servo, motor

spd = pulseio.PWMOut(board.D13)
spd.duty_cycle = 0
dir_pin = DigitalInOut(board.D4)
dir_pin.direction = Direction.OUTPUT

#spd.duty_cycle = 0

#initialize connection between imu and microcontroller
i2c = busio.I2C(board.SCL, board.SDA)
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

sensor = adafruit_bno055.BNO055(i2c)

#spi bus to write and read data from SD card
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)

#chip select output, pin 12 for adafruit
cs = digitalio.DigitalInOut(board.D12)

#create microSD card object and filesystem object
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)

#mount sdcard filesystem into circuitpython filesystem
storage.mount(vfs, "/sd")

fins_deployed = False
fins_retracted = False
launch_detected = False

while True:
    #send these values to SD card
    print('Temperature: {} degrees C'.format(sensor.temperature))
    print('Accelerometer (m/s^2): {}'.format(sensor.acceleration))
    print('Magnetometer (microteslas): {}'.format(sensor.magnetic))
    print('Gyroscope (rad/sec): {}'.format(sensor.gyro))
    print('Euler angle: {}'.format(sensor.euler))
    print('Quaternion: {}'.format(sensor.quaternion))
    print('Linear acceleration (m/s^2): {}'.format(sensor.linear_acceleration))
    print('Gravity (m/s^2): {}'.format(sensor.gravity))
    print()

    with open("/sd/adas.txt", "a") as f:
        t = sensor.temperature
        c = sensor.calibrated
        g = sensor.gravity

            #f.write(str(t))
            #f.write(str(c))
            #f.write(str(g))
        f.write('Temperature: {} degrees C'.format(sensor.temperature))
        f.write('\n\n')
        f.write('Accelerometer (m/s^2): {}'.format(sensor.acceleration))
        f.write('\n\n')
        f.write('Magnetometer (microteslas): {}'.format(sensor.magnetic))
        f.write('\n\n')
        f.write('Gyroscope (rad/sec): {}'.format(sensor.gyro))
        f.write('\n\n')
        f.write('Euler angle: {}'.format(sensor.euler))
        f.write('\n\n')
        f.write('Quaternion: {}'.format(sensor.quaternion))
        f.write('\n\n')
        f.write('Linear acceleration (m/s^2): {}'.format(sensor.linear_acceleration))
        f.write('\n\n')
        f.write('Gravity (m/s^2): {}'.format(sensor.gravity))
        f.write('\n\n\n')

    '''if sensor.linear_acceleration[2] > 50:
        launch_detected = True

    if (not fins_deployed) and launch_detected and sensor.linear_acceleration[2] < 5:
    #if (not fins_retracted) and sensor.linear_acceleration[2] < 1:
        spd.duty_cycle = 6000
        time.sleep(1)
        fins_deployed = True
        print("1")
        spd.duty_cycle = 0
        time.sleep(10)
        dir_pin.value = not dir_pin.value
        spd.duty_cycle = 6000
        time.sleep(2)
        fins_retracted = True
        spd.duty_cycle = 0



    #if fins_deployed and (not fins_retracted) and sensor.linear_acceleration[2] < 2:
    #if fins_deployed and (not fins_retracted) and sensor.linear_acceleration[2] < 1:
        #dir_pin.value = not dir_pin.value
        #spd.duty_cycle = 6000
        #time.sleep(2)
        #fins_retracted = True
        #print("2")
        #spd.duty_cycle = 0 '''


    #with open("/sd/adas.txt", "r") as f:
        #lines = f.readlines()
        #for line in lines:
            #print(line)

    time.sleep(2)