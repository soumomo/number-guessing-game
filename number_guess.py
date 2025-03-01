import random

def main():
    print("Welcome to the number guessing game!")
    while True:
        play_game()
        user_input = input("Do you want to continue playing more rounds?(yes/no)" ).lower().strip()
        if user_input != "yes":
            print("Thank you for playing! Goodbye!")
            break
        else:
            continue
            

    
def play_game():
    number_of_rounds = int(input("How many rounds of the game you want to play?"))
    print(f"Okay we will have a game of rounds of {number_of_rounds}")
    total_score = 0
    for rounds in range(1,number_of_rounds+1):
            lower_bound = random.randint(1, 5)
            upper_bound = random.randint(6, 10)
            number_to_guess = random.randint(lower_bound, upper_bound)
            print(f"Round {rounds}: Guess the number between {lower_bound} and {upper_bound}, inclusive.")

            error_count = 0
            while error_count<2:
                try:
                    guess = int(input("Enter your guess: "))

                    if guess < lower_bound or guess > upper_bound:
                        print(f"WTF! Enter a number between the {lower_bound} and {upper_bound}")
                        total_score -= 1
                        break

                    if lower_bound < guess < number_to_guess:
                        print("Too Small!")
                        print(f"The random number was {number_to_guess}.")
                        total_score -= 1
                    elif number_to_guess< guess < upper_bound:
                        print("Quite Big!")
                        print(f"The random number was {number_to_guess}.")
                        total_score -= 1
                    else:
                        print(f"Congratulations! Round {rounds} cleared!) ")
                        total_score += 5
                    break

                except ValueError:
                    error_count += 1
                    if error_count<2:
                        print(f"You need to enter an integer in the given range [{lower_bound},{upper_bound}]! You have one more chance for this round.")
                    else:
                        print(f"You need to enter an integer in the given range! Moving to next round.")
                        total_score -= 1

    print("You have completed all the rounds!")
    print(f"Your final score is {total_score}!")
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
