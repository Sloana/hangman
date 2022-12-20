
import random
import numpy as np
# Create a list called fruits with five elements
fruits=["apple","peach","banana","pear","grapes"]
word_list=list()

word_list=fruits

word=random.choice(word_list)
# randomly select a word from list word_list
#print(word)
#initialize the word_guessed list
word_guessed=list(['_' for x in range(len(word))])
#initialize the list_of_guesses
list_of_guesses=list()
           
class Hangman:
    """ Create the class Hangman with two parameters word list and num_lives.
    Hangman class has two methods: 1. check_guess(guess) with guess as parameter and
 ask_for_input() with no parameters.
 Check_guess(guess) method checks if the guess letter is in the word and if it is then it replace the '_'in the word_guessed with the letter itself.
 If the guess letter is not in the word then it allows (num_lives-1) more time to guess another letter.
 
 ak_for_input() method"""
    def __init__(self,word_list,num_lives=5):
        self.word_list = word_list
        
        self.num_lives = num_lives
        self.num_letters=np.sum(x=='_' for x in word_guessed)

       
    def check_guess(self,guess):
       
        self.num_letters=np.sum(x=='_' for x in word_guessed)
        while self.num_letters>0:
            if(guess in word):
                print(f"Good guess! {guess} is in the word.")
                for i in range (0,(len(word))):

                    if (word[i]==guess):
                        word_guessed[i]=guess
                        self.num_letters=self.num_letters-1
                        print(self.num_letters)

                list_of_guesses.append(guess)
            else:
                self.num_lives=self.num_lives-1
                print(f'Sorry,{guess} is not in the word {word}')
                print(f'you have {self.num_lives} number of lives left')
            print(word_guessed)
            return word_guessed

    def ask_for_input(self):
        
        while True:
             if self.num_letters>0:
                if self.num_lives>0:
                    guess=input("Enter a letter=")
                    if(len(guess)>1):
                        print("Invalid letter.Please enter a single alphabetical character.")
                    elif (guess in list_of_guesses):
                        print("You already tried that letter")
                    else:

                        self.check_guess(guess)
                        list_of_guesses.append(guess)
                else:
                    break
             else: 
               break
 
def play_game(word_list):
    game=Hangman(word_list)
    guess=game.ask_for_input()
    while True:

        if (game.num_lives==0):
            print("You lost")
        elif game.num_letters>0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
        return game.ask_for_input()

        
play_game(word_list)