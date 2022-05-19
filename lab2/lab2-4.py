import RPi.GPIO as GPIO
import time

button_pin = 24
led_pin = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(led_pin, GPIO.OUT)

button_press = False

#button_callback 함수 정의
def button_callback(channel):
    global button_press
    
    if button_press == False:
        print("Bouncing Test - 1")
    else:
        print("Bouncing Test - 2")
        
    button_press = not button_press

#Event 알림 방식으로 GPIO 핀의 Rising 신호를 감지하면 button_callback 함수 실행
GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback, bouncetime=300)

while 1:
    time.sleep(0.1)
