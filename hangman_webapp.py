"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

global state
state = {'guesses':[],
		 'word':"interesting",
		 'word_so_far':"-----------",
		 'done':False}

@app.route('/')
@app.route('/main')
def main():
	return render_template("hangman.html")
@app.route('/bios')
def team_bios():
	return render_template('bios.HTML')
@app.route('/about')
def intro():
	return render_template('about.html')
@app.route('/start')
def start():
	global state
	state['word'] = hangman_app.generate_random_word()
	state['guesses'] = []
	word_so_far = hangman_app.get_word_so_far(state['word'])
	state['word_so_far'] = word_so_far
	print(state)
	return render_template("play.html",state=state)

@app.route('/play',methods=['GET','POST'])
def play_hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return start()

	elif request.method == 'POST':
		letter = request.form['guess']
		# check if letter has already been guessed
		# and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them
		state['guesses'] += [letter]
		print(state)
		return render_template('play.html',state=state)




if __name__ == '__main__':
	app.run('127.0.0.1',port=3000)
