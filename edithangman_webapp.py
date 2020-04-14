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
	return render_template('hangman.html')

@app.route('/start')
def play():
	global state
	state['word']=hangman_app.generate_random_word()
	state['guesses'] = []
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	want_to_play = True
    while (want_to_play):
        guessed_lettersright= []
        rightcounter=0
        guessed_letterswrong= []
        guesses_left = 10
        letter = 'word'
        done = False
        while not done:
            if letter in guessed_letterswrong or letter in guessed_lettersright:
                guesses_left-=1

            elif letter not in guess:
                guessed_letterswrong.append(letter)
                guesses_left-=1
            else:
                guessed_lettersright.append(letter)
                guesses_left-=1
                rightcounter+=1

            if guesses_left==0:
                done=True
            if counter==rightcounter:
                done=True
                break
            else:
                print(guessed_letterswrong)

                #print the word with a dash for each letter not in guessed_letters"
                letter = input("Type in another letter")
            def is_letter_in_word(check,guesses):
                for letter in check:
                    if letter not in check:
                        print("this letter is in the word")
                        return False
                return True
	global state
	if request.method == 'GET':
		return play()

	elif request.method == 'POST':
		letter = request.form['guess']
		# check if letter has already been guessed
		# and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them
		state['guesses'] += [letter]
		return render_template('play.html',state=state)




if __name__ == '__main__':
    app.run('127.0.0.1',port=3000)
