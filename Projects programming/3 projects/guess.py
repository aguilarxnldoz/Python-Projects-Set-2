"""
This program gives us two games where 
either the user or the computer has to guess 
a secret number, and whenever the answer is incorrect
the user or computer will tell you if it is
too high, or too low until you're correct.
"""


#This will randomize the secret number that is to be guessed.
import random 

#This will ask which of the two games should be played.
game =  input("Select a game [user or comp]: ")

#This is the function for the first game where you have to guess.
def c_guess(x):
    r_num = random.randint(1, x)
    guess = 0

    while guess != r_num:
        guess = int(input(f"Enter a random number between 1 and {x}: "))

        if guess > r_num:
            print("Guess is too high, guess again.")

        elif guess < r_num:
            print("Guess is too low, guess again.")

    print("Number has been guessed, excellent!")

#This is the function for the second game where the computer guesses your number.
def u_guess(x):
    low = 1
    high = x
    fb = ''

    while fb != 'p':
        if low != high:
            estimate = random.randint(low, high)
        else:
            estimate = low
        fb = input(f"Is {estimate} low, high, or correct?: ")
        if fb == "low": 
            low == estimate + 1
        elif fb == "high":
            high == estimate - 1
        elif fb == "correct":
            print("I have estimated your number!")
            break
        else:
            print("invalid option, try again.")


        
if game == "comp":
    c_guess(100)

elif game == "user":
    u_guess(100)

elif game == "q":
    print("See you next time.")

else:
    while game != "comp" or "user" or "q":
        print('Invalid Option.')