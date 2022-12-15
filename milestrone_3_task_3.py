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


def ask_for_input(guess,word):
    nr=0
    guess=check_guess(guess)
    for i in (0,len(word)-1):
        if (word[i]==guess):
            nr+=1
    if (nr!=0):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again." )
    

ask_for_input(guess,word)