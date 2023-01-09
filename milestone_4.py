#Task 1
fruits=["apple","peach","banana","pear","grapes"]
word_list=fruits
print("My favorite fruits are:",word_list)
confirmation = True
guess=input("Enter a letter")
#Task 2
import random
word=random.choice(word_list)
print(word)
len(word)
def check_guess(guess):
    lguess=guess.lower()
    return lguess

word_g=[]
import _random
class Hangman:
    def __init__(self,word_list,num_lives=5):
        word=random.choice(self.word_list)

    def word_guessed(guess,word):
        for i in len(word):
            if word[i]==guess:
                word_g[i]=guess
            else:
                word_g[i]='_'

h1=Hangman(word_list,num_lives=5)
print(h1.word_guessed(guess))