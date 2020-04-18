"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
import csv
import random
cool = []
f = open('words 3.csv')
words = csv.reader(f)
for row in words:
    cool.append(row)


def generate_random_word():
    cool = []
    f = open('words 3.csv')
    words = csv.reader(f)
    for row in words:
        cool.append(row)
    theword = str(random.choice(cool))
    guess = theword[2:][:-2]
    unique = ''.join(set(guess))
    check = list(unique)
    print(len(guess))
    counter=len(unique)
    return guess

def get_word_so_far(word):
    word_so_far = '-' * len(word)
    return word_so_far

def play_hangman():
    want_to_play = True
    while (want_to_play):
        guessed_lettersright= []
        rightcounter=0
        guessed_letterswrong= ["-","-","-","-","-","-"]
        guesses_left = 10
        letter = input("Please input a letter >")
        done = False
        blanks = "- "*len(guess)
        print(blanks)
        while not done:
            if letter in guessed_letterswrong or letter in guessed_lettersright:
                guesses_left-=1
                print("You have already guessed that letter, guess another one!")

            elif letter not in guess:
                guessed_letterswrong.remove("-")
                guessed_letterswrong.append(letter)
                print("This letter is not in the word, guess again.")
                guesses_left-=1
                #add letter to guessed letters"
                #tell user the letter is not in the word"
                #subtract one from the guesses_left"
            else:
                guessed_lettersright.append(letter)
                guesses_left-=1
                rightcounter+=1
                print("This letter is in the word!")
                #add letter to guessed letters"
                #tell user the letter is in the word"

            if guesses_left==0:
                print("The number of guesses left is zero, You lose!")
                done=True
            #set done to be true and tell the user they lost!"
            if counter==rightcounter:
                print("You got the word correct! It was"+guess+ ". You win!")
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
            #def is_guess_correct(check, guesses):
                #for let

                #all the letters in the word have been guessed"
                #set done to be true and tell the user they won!"
            is_letter_in_word(check, guessed_lettersright)
        want_to_play = input("Do your want to play Hangman?\nType 'done' to quit: \n")
        if want_to_play == "Done" or want_to_play == "done":
            done = True
            break
if __name__ == '__main__':
    play_hangman()
