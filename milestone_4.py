import random
word_list=list()
word_list=["apple","peach","banana","pear","grapes"]

class Hangman:
    def __init__(self,word_list,num_lives=5):

        self.word_list = word_list
        self.word=random.choice(word_list)
        self.word_guessed=list(['_' for x in range(len(self.word))])
        self.list_of_guesses=[]
        self.num_lives = num_lives
        self.num_letters=len(set(self.word))

    # Create check(guess) that checks if the gues letter is in the selected word
    def check_guess(self,guess):

        if(guess in self.word):
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):

                if (letter==guess):
                    self.word_guessed[i]=guess
                    self.word_guessed[i]=letter
            self.num_letters-=1

        else:
            self.num_lives=self.num_lives-1
            print(f'Sorry,{guess} is not in the word {self.word}')
            self.num_lives-=1
            print(f'you have {self.num_lives} number of lives left')

    # Create function ask_for_input(), which ask the user for a letter ssigned to guess variable and checks if the letter is a valid letter. Inside the function ask_for_input() is called  check(guess) function.
    def ask_for_input(self):
         while True:
            guess=input("Enter a letter=")
            if(len(guess) != 1 and guess.isalpha()):
                print("Invalid letter.Please enter a single alphabetical character.")
            elif (guess in self.list_of_guesses):
                print("You already tried that letter")
            else:

                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

h1=Hangman(word_list)
h1.ask_for_input()
