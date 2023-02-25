from crypt import methods
from urllib import response
import requests, random
from flask import render_template, redirect, request, session, flash
from Flask_app import app
from Flask_app.models.user import Person
from datetime import date, timedelta
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
	return render_template('login.html')

@app.route('/Reg')
def page():
	return render_template('Reg.html')


@app.route('/Register', methods = ['POST'])
def Register():
	data = {
		"first_name": request.form['first_name'],
		"last_name": request.form['last_name'],
		"email": request.form['email'],
		"password": bcrypt.generate_password_hash(request.form['password'])
	}
	id = Person.save(data)
	session['user_id'] = id
	return redirect('/dash')

@app.route('/login', methods = ['POST'])
def login():
	user = Person.get__by_email(request.form)
	if not user:
		flash ("Wrong Email", "login")
		return redirect('/')
	if not bcrypt.check_password_hash(user.password, request.form['password']):
		flash('Password incorrect', 'login')
		return redirect('/')
	session['user_id'] = user.id
	return redirect('/dash')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('/')

@app.route('/dash')
def Dash():
	today = date.today()+timedelta(1)
	return render_template('dash.html', today = today)
	
@app.route('/acc')
def account():
	# user = Person.get_by_id()
	return render_template('account.html')




@app.route('/roll/killer')
def roll_killer():
	response = request.get('https://dbd.tricky.lol/api/randomperks?role=survivor')
	session['name'] = []
	session['name'].append(response)
	print(session['name'])
	return redirect(('/dash'))

@app.route('/roll')
def roller():
	Survivor_Perks = ['Bond', 'Prove Thyself', 'Leader', 'Quick & Quiet', 'Sprint Burst', 'Empathy', 'Botany Knowledge', 'Self-Care', 'Iron Will', 'Calm Spirt', 'Saboteur', 'Balanced Landing', 'Urban Evasion', 'Streetwise', 'Sole Survivor', 'Object of Obsession', 'Decisive Strike', 'Open-Handed', 'Up the Ante', 'Ace in the Hole', 'Left Behind', 'Borrowed Time', 'Unbreakable', 'Techniciaan', 'Lithe', 'Alert', "We're Gonna Live Forever", 'Dead Hard', 'No Mither', 'Wake Up!', 'Pharmacy', 'Vigil', 'Tenacty', "Detective's Hunch", 'Stake Out', 'Dance With Me', 'Windows of Opportunity', 'Boil Over', 'Diversion', 'Deliverance', 'AutoDidact', 'Breakdown', 'Aftercare', 'Distortion', 'Solidarity', 'Poised', 'Head On', 'Flip-Flop', 'Buckle Up', 'Mettle of Man', 'Situational Awareness', 'Self-Aware', 'Inner Healing', 'Guardian', 'Kinship', 'Renewal', 'Lucky Break', 'Any Means Necessary', 'Breakout', 'Off the Record', 'Red Herring', 'For the People', 'Soul Guard', 'Blood Pact', 'Repressed Alliance', 'Visionary', 'Desperate Measures', 'Built to Last', 'Appraisal', 'Deception', 'Power Struggle','Fast Track', 'Smash Hit', 'Self-Preservation', 'Counterforce', 'Resurgence', 'Blast Mine', 'Bite the Bullet', 'Flashbang', 'Rookie Spirit', 'Clairvoyance', 'Boon: Circle of Healing', 'Boon: Shadow Step', 'Overcome', 'Corrective Action', 'Boon: Exponential', 'Parental Guidance', 'Empathic Connection', 'Boon: Dark Theory', 'Inner Focus', 'Residual Manifest', 'Overzealous', 'Wiretap', 'Reactive Healing', 'Low Profile', 'Better than New', 'Reassurance', 'Hyperfocus', 'Potential Energy', 'Fogwise', 'Quick Gambit', 'Dark Sense', 'Déjà Vu', 'Hope', 'Kindred', 'Lightweight', 'No One Left Behind', "Plunderer's Instinct", 'Premonition', 'Resillience', 'Slippery Meat', 'Small Game', 'Spine Chill', 'This Is Not Happening', "We'll Make It", ]
	session['surv_perks'] = []
	for number in Survivor_Perks:
		session['surv_perks'].append(number)
	for y in range(1, 5, 1):
		y = random.choice(session['surv_perks'])
		session['surv_perks'].append(y)
		print(y)
	return redirect('/dash')

# @app.route('/roll')
# def roller():
# 	response = requests.get('https://dead-by-api.herokuapp.com/api/perks/surv')
# 	session['perks'] = []
# 	name = []
# 	for _ in range(4):
# 		a = response.json()['data'][random.randint(0, len(response.json()['data']) - 1)]['name']
# 		session['perks'].append(a)	
# 	return redirect(('/dash'))


	# .__dict__

@app.route('/reset')
def new():
    session.clear()
    return render_template('dash.html')