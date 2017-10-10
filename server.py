from flask import Flask, redirect, request, render_template, flash

app = Flask(__name__)
app.secret_key = 'hushhush'

@app.route('/')
def showForm():
	return render_template('index.html')


@app.route('/result', methods=['POST'])
def showResult():
	status = True
	if len(request.form['name']) < 1:
		flash("Name cannot be empty!")
		status = False
	if len(request.form['comment']) > 120:
		flash("Cannot exceed 120 characters")
		status = False
	if status == False:
		return redirect('/')
	name = request.form['name']
	dojo = request.form['dojo']
	lang = request.form['lang']
	comment = request.form['comment']
	return render_template('submit.html', name=name, dojo=dojo, lang=lang, comment=comment)

@app.route('/sendback', methods=['POST'])
def sendBack():
	back = request.form['submit']
	print('clicked')
	return redirect('/')

app.run(debug=True)