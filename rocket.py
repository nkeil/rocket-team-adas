import board
import digitalio
import time
import busio
import adafruit_bno055

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bno055.BNO055(i2c)
f = open('data.txt', a)
f.write('{:5}'.format('#'))
f.write('{:10}'.format('AccX'))
f.write('{:10}'.format('AccY'))
f.write('{:10}'.format('AccZ'))
f.write('{:10}'.format('EulerX'))
f.write('{:10}'.format('EulerY'))
f.write('{:10}'.format('EulerZ'))
f.write('\n')
i = 1

# seconds in between each reading
sec_interval = 1.0

# coefficients
Kp = 1.0
Ki = 1.0
Kd = 1.0

last_exp_al = 0.0

while True:
    f.write('{:5d}: '.format(i))
    f.write('{:9.5f} '.format(sensor.acceleration[0]))
    f.write('{:9.5f} '.format(sensor.acceleration[1]))
    f.write('{:9.5f} '.format(sensor.acceleration[2]))
    f.write('{:9.5f} '.format(sensor.euler[0]))
    f.write('{:9.5f} '.format(sensor.euler[1]))
    f.write('{:9.5f}'.format(sensor.euler[2]))
    f.write('\n')

    # sensor.temperature
    # sensor.magnetic
    # sensor.gyro
    # sensor.quaternion
    # sensor.linear_acceleration
    # sensor.gravity

    exp_al = 1.0 # todo
    error = 4000 - exp_al

    p_term = Kp * error
    i_term += Ki * error
    d_term = 0.0 if last_exp_al == 0.0 else (exp_al - last_exp_al) / sec_interval

    output = p_term + i_term + d_term 

    last_exp_al = exp_al
    ++i
    # break condition
    time.sleep(sec_interval)

f.close()