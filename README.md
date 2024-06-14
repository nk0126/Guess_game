# Guess_game
Guess Game
Overview
This is a simple number guessing game written in Python. The game allows users to select a difficulty level and then attempts to guess a randomly generated number between 1 and 100. The user receives feedback after each guess, indicating whether their guess is too high or too low. The game continues until the user either guesses the number correctly or exhausts their attempts.

How to Play
Choose a Difficulty Level:

The game offers two difficulty levels: "low" and "hard".
When prompted, type "low" for an easier game with more attempts (10 attempts).
Type "hard" for a more challenging game with fewer attempts (5 attempts).
Make Your Guess:

After selecting the difficulty level, you will be prompted to guess a number between 1 and 100.
Enter your guess and press Enter.
Receive Feedback:

After each guess, you will be told if your guess is too high, too low, or correct.
If your guess is correct, the game will congratulate you and reveal the number.
If your guess is incorrect, you will be prompted to guess again, and the number of attempts left will be displayed.
Game Over:

The game ends when you either guess the number correctly or run out of attempts.
If you run out of attempts without guessing correctly, the game will reveal the correct number.
****************************************
!! Welcome to Guess Game !!
****************************************
choose your game difficulty level (low, hard) :- low

guess a number from 1 to 100 (Okey Great you have 10 attempts left ) :- 50

It's Too high !!

guess a number from 1 to 100 (Okey Great you have 9 attempts left ) :- 25
It's Too low

guess a number from 1 to 100 (Okey Great you have 8 attempts left ) :- 37
Hurry!! you guess a correct number is 37

Code Explanation
check_answer()
This function is the main logic of the game. It includes the following steps:

Generate a random number between 1 and 100 using randint.
Prompt the user to choose a difficulty level (low or hard).
Set the number of attempts based on the chosen difficulty level.
Loop through the number of attempts, allowing the user to guess the number each time.
Provide feedback on each guess (too high, too low, or correct).
End the game when the user guesses correctly or runs out of attempts.
print("*"*40)
This line is used to print a decorative border for the game welcome message and game over message, making the console output more readable and visually appealing.

Running the Game
To run the game, simply execute the script in a Python environment. Ensure you have Python installed, and then run the following command in your terminal:

python guess_game.py

Contributions
Feel free to contribute to this project by submitting pull requests. Any improvements or bug fixes are welcome.

License
This project is licensed under the MIT License - see the LICENSE file for details.

