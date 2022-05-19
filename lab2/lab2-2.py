import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm_led = GPIO.PWM(18, 500) # 초기화, frequency=500Hz
pwm_led.start(100) # Duty Cycle 초기값 설정

while (True):
	duty_input = input("Brightness: ")
	duty_value = int(duty_input)
	if duty_value > 100:
		print("Wrong Value. Enter 0 to 100")
	else:
		pwm_led.ChangeDutyCycle(duty_value) # 밝기 값 변경
	time.sleep(1)
	
GPIO.cleanup()
