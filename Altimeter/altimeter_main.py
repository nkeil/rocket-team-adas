from MS5607 import MS5607

sensor = MS5607()
f = open("demofile2.txt", "a")


t2 = time.time()
t1 = time.time()
while (True):
	temperature = sensor.getDigitalTemperature()
	pressure = sensor.getDigitalPressure()
	converted = sensor.convertPressureTemperature(pressure, temperature)
	altitude = sensor.getMetricAltitude(converted, sensor.inHgToHectoPascal(29.95)) #set the altimeter setting appropriately
	t2 = time.time()
	f.write( str(t2 - t1) + "            " + str(altitude))
	t1 = t2

f.close()
