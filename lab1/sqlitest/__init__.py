from flask import Flask, request, url_for, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Phonenum(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	phone = db.Column(db.String(40))
	
	def __init__(self, id=1, name=None, phone=None):
		self.id = id
		self.name = name
		self.phone = phone
	
	def __repr__(self):
		return '<%r, %r>' %	(self.name,self.phone)


@app.route('/show')
def show():
	row = db.session.query(Phonenum).all()
	if row:
		return render_template('phoneshow.html',	items=row)
	return abort(404, "Page not found")


@app.route('/show/name/<item>')
def showname(item):
	row = db.session.query(Phonenum).filter(Phonenum.name.like("%"+item+"%")).all()
	print(row)
	if row:
		return render_template('phoneshow.html', items=row)
	return abort(404, "Page not found")

@app.route('/show/phone/<item>')
def showphone(item):
	row = db.session.query(Phonenum).filter(Phonenum.phone.like("%"+item+"%")).all()
	print(row)
	if row:
		return render_template('phoneshow.html', items=row)
	return abort(404, "Page not found")