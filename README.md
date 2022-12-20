# Hangman
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain number of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 
The attributes iniialized are 
1. word: The word randomly picked from the word_list which must be guessed. 
2. word_guessed: A list of the letters of the word, with _ for each letter not yet guessed. 
3. num_letters: The number of UNIQUE letters in the word that have not been guessed yet.
4. num_lives: The number of lives the player has at the start of the game.
5. word_list: A list of words.
6. list_of_guesses: A list of the guesses that have already been tried. Set this to an empty list initially.
7. guess: the letter guessed by the user
## Class and methods
Hangman class is word_list and num_lives as parameters. 
Also two methods have been defined ask_for_input() which will ask the user to guess a letter and check_guess() and that will check if the guess is in the word.
1. ask_for_input() asks for an input letter. It also checks if the letter is an valid letter and also if it has been been already tried before.
2. check_guess(guess) check if the guessed letter is in the word. if the guessed letter is not in the word, then it allows the uses (num_lives -1) more time to try. 

3. play_game(word_list) function define an object of the Hangman class and based on num_lives and num_letters left it defines the output:
"You lost!" or "Congratulations. You won the game!"
