from flask import Flask, render_template,request,make_response,url_for, redirect,session, flash, abort

import os

from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'cGFzc2FueXRoaW5nenp6XzIzNA=='


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.route('/')
def index():
	search = request.args.get('search')
	if not search:
		return render_template('index.html')
	return render_template('index.html', username=search)

#default setting
@app.route('/profile/')
def show_profile_default():
	return render_template('profile.html')

#dinamis
@app.route('/profile/<username>')
def show_profile_username(username):
	return render_template('profile.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def show_login():
	if request.method == 'POST' and request.form['user'] == 'admin' and request.form['password'] == 'admin':
		#resp = make_response('Username kamu adalah ' + request.form['user'])
		#resp.set_cookie('user', request.form['user'])

		if request.form['password'] == '':
			abort(404)

		session['user'] = request.form['user']
		flash('Loggin Success', 'success')
		#return resp
		return redirect(url_for('show_profile_username', username=session['user']))


	if 'user' in session:
		username = session['user']
		return redirect(url_for('show_profile_username', username=username))
	return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('user', None)
	return redirect(url_for('show_login'))


@app.route('/getcookie')
def getCookie():
	username = request.cookies.get('user')
	return 'Username kamu adalah ' + username

ALLOWED_EXTENSION = set(['png','jpeg','jpg','gif'])
app.config['UPLOAD_FOLDER'] ='uploads'


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION



@app.route('/uploadfile', methods=['GET', 'POST'])
def uploadfile():
	if request.method == 'POST':

		file = request.files['file']

		if 'file' not in request.files:
			return render_template('upload_gagal.html')


		if file.filename  == '':
			return render_template('upload_gagal.html')

		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(app.config['UPLOAD_FOLDER'] + filename)
			return render_template('upload_sukses.html')

	return render_template('upload.html')


