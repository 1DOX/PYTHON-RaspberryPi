import Adafruit_DHT
import sys
from PySide2 import QtCore, QtWidgets, QtGui, QtXml, QtUiTools

sensor = Adafruit_DHT.DHT22
pin=18

class MainWindow(QtWidgets.QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("TEMP & HUMI")
		self.setup_ui()
		
	def setup_ui(self):
		#main_layout = QtWidgets.QVBoxLayout()
		main_layout = QtWidgets.QFormLayout()
		
		label_temp = QtWidgets.QLabel("Temperature: ")
		label_humi = QtWidgets.QLabel("Humidity: ")
		self.temp = QtWidgets.QLineEdit("")
		self.humi = QtWidgets.QLineEdit("")
		
		main_layout.addRow(label_temp, self.temp)
		main_layout.addRow(label_humi, self.humi)
		
		self.getTemp()
		
		self.setLayout(main_layout)
		self.show()
		
	def getTemp(self):
		humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
		if humidity is not None and temperature is not None:
			self.setTemp(temperature, humidity)
			print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
		else:
			print('Failed to get reading. Try again!')
			
	def setTemp(self, temp, humi):
		self.temp.setText('{0:0.1f}*C'.format(temp))
		self.humi.setText('{0:0.1f}%'.format(humi))
		

if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	main = MainWindow()
	sys.exit(app.exec_())
