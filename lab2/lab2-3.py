from flask import Flask, render_template_string
import RPi.GPIO as GPIO
import time

buzzer = 18
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) # runtime warning 무시
GPIO.setup(buzzer, GPIO.OUT)

pwm = GPIO.PWM(buzzer, 1.0) # 초기 주파수 1.0Hz
app = Flask(__name__)

C = 261 # 도
D = 293 # 레
E = 329 # 미
F = 349 # 파
G = 391 # 솔
A = 440 # 라
B = 493 # 시
C2 = 523 # 도

def play_piano(num):
	pwm.ChangeFrequency(num)
	time.sleep(0.3)
	pwm.stop()

control_page = """
<script>
function changed(id)
{
window.location.href='/' + id
}
</script>
<h1>Buzzer Control</h1>
<input type='button' onClick='changed({{piano_c}})'
value='C {{piano_c}}'/>
<input type='button' onClick='changed({{piano_d}})'
value='D {{piano_d}}'/>
<input type='button' onClick='changed({{piano_e}})'
value='E {{piano_e}}'/>
<input type='button' onClick='changed({{piano_f}})'
value='F {{piano_f}}'/>
<input type='button' onClick='changed({{piano_g}})'
value='G {{piano_g}}'/>
<input type='button' onClick='changed({{piano_a}})'
value='A {{piano_a}}'/>
<input type='button' onClick='changed({{piano_b}})'
value='B {{piano_b}}'/>
<input type='button' onClick='changed({{piano_c2}})'
value='C2 {{piano_c2}}'/>
"""

@app.route('/')
@app.route('/<piano>')
def index(piano="n"):
	if piano != "n" and piano != "favicon.ico" :
		pwm.start(90.0) # duty cycle 90%
		num = int(piano)
		play_piano(num)
	return render_template_string(control_page, piano_c=C, piano_d=D, piano_e=E, piano_f=F, piano_g=G, piano_a=A, piano_b=B, piano_c2=C2)

if __name__ == '__main__' :
	app.run(host='localhost', port=8080)

