import random
word_list=list()
word_list=["apple","peach","banana","pear","grapes"]

word=random.choice(word_list)

guess=input("Enter a letter")
if len(guess)==1:
    print("Valid letter!")
else:
    print( "Invalid letter. Please, enter a single alphabetical character.")

    
if guess in word:
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again." )

# Create check(guess) that checks if the gues letter is in the selected word
def check_guess(guess):
    guess=guess.lower()
    if(guess in word):
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again." )

    return guess

# Create function ask_for_input(), which ask the user for a letter ssigned to guess variable and checks if the letter is a valid letter. Inside the function ask_for_input() is called  check(guess) function.
def ask_for_input():
   while True:
    guess=input("Enter a letter")
    if len(guess)==1:
        print("Valid letter!")
    else:
        print( "Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
    break

ask_for_input()