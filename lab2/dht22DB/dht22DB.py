import Adafruit_DHT
import sqlite3
import datetime

conn = sqlite3.connect('dht22.db')
c = conn.cursor()

sensor = Adafruit_DHT.DHT22
pin=18

#c.execute("CREATE TABLE dht22 (time TEXT PRIMARY KEY, temp TEXT, humi TEXT )")

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
if humidity is not None and temperature is not None:
	print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
	c.execute('INSERT INTO dht22 VALUES(?, ?, ?)', (datetime.datetime.now(), temperature, humidity))
else:
	print('Failed to get reading. Try again!')
	
conn.commit()
conn.close()
exit()
