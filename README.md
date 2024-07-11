# Software Development At Prodigy Infotech
## Task 2 :

Build a program that generates a random number and challenges the user to guess it. The program should prompt the user to input their guess, compare it to the generated number, and provide feedback if the guess is too high or too low. It should continue until the user correctly guesses the number and then display the number of attempts it took to win the game.


# Dependencies :

1. Python 3.12
2. PySide6
3. Random

# Project Overview
## Objectives:

1. **User Interaction**: Create an engaging game where players can guess a randomly selected number..
2. **Input and Feedback**: Allow players to enter their guesses and receive instant feedback.
3. **Guidance**: Inform players if their guesses are too high or too low to help them reach the correct answer.
4. **Success Acknowledgment**: Celebrate when the player guesses correctly.
5. **Game Reset**: Start a new game automatically after a correct guess to encourage continued play.

# Project Structure
## Main Interface:

1. **Title and Instructions**: Display the game title and instructions for the player.
2. **Input Field**: Provide a space where players can type their guess.
3. **Submit Button**: A button to submit the player's guess.
4. **Feedback Display**: Show feedback based on the player's guess, indicating whether it was too high, too low, or correct.

## Game Logic:

1. **Random Number Generation**: At the start of each game, select a random number for the player to guess.
2. **Guess Validation**: Check if the player's guess matches the target number, and provide appropriate feedback.
3. **Feedback Mechanism**: Inform the player if their guess is higher or lower than the target number.
4. **Winning Condition**: If the player's guess is correct, acknowledge their success and start a new game.

# Implementation Details
## Interface Setup:

1. Create the main window where the game will be displayed.
2. Add text fields and buttons for user interaction.
3. Use labels to show instructions and feedback to the player.

## Game Flow:

1. When the game starts, generate a random number.
2. The player types a guess and submits it.
3. The game checks the guess and provides feedback.
4. If the guess is incorrect, the player tries again.
5. If the guess is correct, the game congratulates the player and starts a new round.

## Feedback and Messages:

1. Inform the player if their input is not a valid number.
2. Guide the player if their guess is too high or too low.
3. Congratulate the player upon guessing the correct number.
4. Reset the game for another round of play.
