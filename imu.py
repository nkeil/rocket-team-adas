import board
import digitalio
import time
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)
#i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

sensor = adafruit_bno055.BNO055(i2c)

while True:
    print(sensor.calibrated)
    print(sensor.temperature)
    print(sensor.gravity)
    time.sleep(2)