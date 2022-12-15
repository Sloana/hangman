
#Task 1
fruits=["apple","peach","banana","pear","grapes"]
word_list=fruits
print("My favorite fruits are:",word_list)

#Task 2
import random
word=random.choice(word_list)
print(word)
len(word)
# # Task 3

# # commit
# # #Task 4
# # if len(guess)==1:
# #     print("Good guess")

# # else:
# #     print("Opps! That is not a valid input")
# # confirmation = True
# # guess=input("Enter a letter")
# # while len(guess)!=1:
# #     print("invalid letter. please enter a single alphabetical character")
# #     guess = input("guess a letter?")

# print(guess)
nr=0
for i in (0,len(word)-1):
    if (word[i]==guess):
        nr+=1
if (nr!=0):
    print(f"Good guess! {guess} is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again." )

print(word)
print(nr)


# Task 3
def check_guess(self,guess):
    self.guess=guess
    return True


def ask_for_input(self,guess,word):
    nr=0
    for i in (0,len(self.word)-1):
        if (self.word[i]==self.guess):
            nr+=1
    if (nr!=0):
        print(f"Good guess! {self.guess} is in the word.")
    else:
        print(f"Sorry, {self.guess} is not in the word. Try again." )
    return True
