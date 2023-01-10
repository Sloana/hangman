# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain number of attempts. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
Hangman game is built Python language.  Hangman class has two parameters word_list and num_lives and initialized attributes as following: 
1.  word: The word randomly picked from the word_list which must be guessed. 
2. word_guessed: A list of the letters of the word, with _ for each letter not yet guessed. 
3. num_letters: The number of UNIQUE letters in the word that have not been guessed yet.
4. num_lives: The number of lives the player has at the start of the game.
5. word_list: A list of words.
6. list_of_guesses: A list of the guesses that have already been tried. Set this to an empty list initially.
The two methods built inside the class are check_guess() and ask_for_input(). 
- ask_for_input() asks the user for input a letter names as guess. This method also checks if the letter is a single or a valid alphabetic letter. Also, this for an input letter. It also checks if the letter is a valid letter and if it has been already tried before.
-  check_guess(guess) is the method that has as argument the guessed letter “guess”. This method check if the guess letter is in the word. Note that word is an randomly word selected from word_list. 1. if the guessed letter is in the word then the letter guessed will replace  “_” in the word_guessed with the letter itself. 
2. if the guessed letter is not in the word, then it allows the user to guess (num_lives -1) more time another letter. 
Finally, the function that  play game(word_list) function that in his body has:
1.	 defined an object of the Hangman class and based on num_lives and num_letters 
and checks if num_lives is 0 then the output is “You lost”:
2.	f the num_letters> 0 then it still ask_for_input()
if both of conditions 1 and 2  are true, then the output is : 
"Congratulations. You won the game!"
