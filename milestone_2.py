import random
word_list=list()
word_list=["apple","peach","banana","pear","grapes"]

print("My favorite fruits are:",word_list)
word=random.choice(word_list)
guess=input("Enter a single letter")
if len(guess)==1:
    if guess.isalpha():
        print("Good guess")
else:
    print("Opps! That is not a valid input")
