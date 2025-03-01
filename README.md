# number-guessing-game
A simple Python command-line number guessing game
# Number Guessing Game

Welcome to the Number Guessing Game! This is a simple console-based game where you will guess a number within a specified range. The game consists of multiple rounds, and you can choose to play multiple rounds in one session.

## How to Play

1. **Start the Game**: Run the `main.py` script to start the game. You will be welcomed with a message.
2. **Choose Number of Rounds**: You will be prompted to enter the number of rounds you want to play.
3. **Guess the Number**: For each round, you will be given a range of numbers. Your task is to guess the number within that range.
   - If your guess is too small or too big, you will be informed.
   - You have two chances to enter a valid integer within the specified range. If you fail to do so, you will lose the round.
4. **Score Points**: Points are awarded based on your guesses:
   - Correct guess: +5 points
   - Incorrect guess: -1 point
5. **Continue Playing**: After completing the specified number of rounds, you can choose to continue playing more rounds or exit the game.
6. **End the Game**: If you choose to stop playing, your final score will be displayed, and the game will end.

## Example

```
Welcome to the number guessing game!
How many rounds of the game you want to play? 3
Okay we will have a game of rounds of 3
Round 1: Guess the number between 2 and 9, inclusive.
Enter your guess: 4
Too Small!
The random number was 7.
Round 2: Guess the number between 1 and 6, inclusive.
Enter your guess: 5
Congratulations! Round 2 cleared!
Round 3: Guess the number between 3 and 8, inclusive.
Enter your guess: 2
WTF! Enter a number between the 3 and 8
You have completed all the rounds!
Your final score is 3!
Thank you for playing!
Do you want to continue playing more rounds?(yes/no) no
Thank you for playing! Goodbye!
```

## Notes

- The range for the number to guess is randomly generated for each round.
- Entering a guess outside the specified range will result in an immediate loss of that round.
- You have two chances to enter a valid integer for each round.

## Requirements

- Python 3.x

## Running the Game

To run the game, execute the following command in your terminal:

```sh
python3 main.py
```

Enjoy the game and happy guessing!
