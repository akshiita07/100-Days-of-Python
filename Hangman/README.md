This project is a Python implementation of the classic Hangman game. It leverages two modules, `hangman_art` and `hangman_words`, to provide the necessary artwork and word list for the game. Here’s a brief description of the project:

1. **Word Selection**:
   - The game randomly selects a word from a predefined word list (`hangman_words.word_list`) and assigns it to the variable `chosen_word`.
   - It then initializes a list of blanks (`blanks`), with each blank representing a letter in the `chosen_word`.

2. **Game Initialization**:
   - The game sets the initial number of lives to 6.
   - The Hangman logo from the `hangman_art` module is printed at the start of the game.

3. **Main Game Loop**:
   - The game runs a while loop that continues until the end of the game (either the player wins or loses).
   - In each iteration, the user is prompted to guess a letter. The guess is converted to lowercase.
   - If the guessed letter has already been guessed, the game informs the user.
   - The game then checks if the guessed letter is in the `chosen_word`:
     - If yes, it reveals the letter in the appropriate positions in the `blanks` list.
     - If no, it decrements the `lives` count and displays the corresponding Hangman ASCII art from the `hangman_art.stages` list.
   - If the `lives` count reaches 0, the game ends with a "You lose" message.
   - If the player successfully guesses all the letters (i.e., no blanks remain), the game ends with a congratulatory message.

4. **Feedback and Continuation**:
   - After each guess, the current state of the `blanks` list is displayed, showing the player their progress.
   - The loop ensures the game continues until a win or loss condition is met.

This project provides a simple yet interactive way to play Hangman, utilizing basic Python constructs such as loops, conditionals, and list operations.
