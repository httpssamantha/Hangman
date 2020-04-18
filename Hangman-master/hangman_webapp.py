"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)
import copy
import time


global state
state = {'first':{'guesses':[],
		 'word':"interesting",
		 'copy': " ",
		 'word_so_far':"-----------",
		 'done':False},
		 'second':{'right':[]}}

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
	state['first']['copy'] = ' '
	state['first']['word'] = hangman_app.generate_random_word()
	state['first']['copy'] = copy.copy(state['first']['word'])
	state['first']['guesses'] = []
	state['first']['word'] = ''.join(set(state['first']['word']))
	word_so_far = hangman_app.get_word_so_far(state['first']['copy'])
	state['first']['word_so_far'] = word_so_far
	state['first']['word'] = list(set(state['first']['word']))
	print(state)
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def play_hangman():
	global state
	okay = len(state['first']['word'])
	hello = len(state['first']['guesses'])
	if request.method == 'GET':
		return start()

	elif request.method == 'POST':
		letter = request.form['guess']
		def is_letter_in_word(check,guesses):
			for letter in check:
				if letter not in check:
					return False
	state['first']['guesses'] += [letter]
	if letter in state['first']['word']:
		state['second']['right'] += letter
	if letter not in state['first']['word']:
		state['first']['guesses'] += letter
	else:
		if len(state['first']['word']) == len(state['second']['right']):
			print("you got it right!")
			print("your word was "+state['first']['copy'])
			state['second']['right'] = []
			state['first']['guesses'] = []
			state['first']['words_so_far'] = "-----------"
			state['first']['word'] = " "
			time.sleep(2)
			return render_template("end.html",state=state)


	print(state)

		# check if letter has already been guessed
		# and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them
		#print(state)
		#for state['guesses'] in state['word']:
			#if len(state['guesses']) >= len(state['word']):

			#if [letter] in state['word']:
				#print("this letter is in the word")
				#elif state['guesses'] == state['word']:
				#print("you got it right!")
		#if state['guesses'] == state['word']:
			#state['done'] = True
			#return render_template("end.html",state=state)

	return render_template('play.html',state=state)




if __name__ == '__main__':
	app.run('127.0.0.1',port=3000)
