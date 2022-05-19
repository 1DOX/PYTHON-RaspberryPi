from flask import Flask, request, url_for, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dht22.db'
db = SQLAlchemy(app)

class Dht22(db.Model):
	time = db.Column(db.String, primary_key=True)
	temp = db.Column(db.String)
	humi = db.Column(db.String)
	
	def __init__(self, time=None, temp=None, humi=None):
		self.time = time
		self.temp = temp
		self.humi = humi
	
	def __repr__(self):
		return '<%r, %r, %r>' %	(self.time, self.temp, self.humi)


@app.route('/')
def show():
	row = db.session.query(Dht22).all()
	if row:
		return render_template('dht22DB.html', items=row)
	return abort(404, "Page not found")
