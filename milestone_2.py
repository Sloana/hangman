#Task 1
fruits=["apple","peach","banana","pear","grapes"]
word_list=fruits
print("My favorite fruits are:",word_list)

#Task 2
import random
word=random.choice(word_list)
print(word)

# Task 3
guess=input("Enter a single letter")
print(guess)
# commit
#Task 4
if len(guess)==1:
    print("Good guess")

else:
    print("Opps! That is not a valid input")