


import random

user = 0
op = 0


def game():

    global op

    print("Answer in all lowercase.")
    match = input("Rock, Paper, Scissors, Lizard or Spock?: ")
    comp = random.choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


    if match == comp:
        return 're-do'
    
    if w(match, comp):
        global user
        user = user + 1
        print("Score: " + str(user) + " - " + str(op))
        return "you're a winner!"
    
    
    
    op = op + 1
    print("Score: " + str(user) + "-" + str(op))
    return "you're a loser..."
        



def w(you, computer):
    if (you == "rock" and computer == "scissors") or (you == "rock" and computer == "lizard") \
        or (you == "lizard" and computer == "paper") or (you == "lizard" and computer == "spock") \
        or (you == "spock" and computer == "rock") or (you == "spock" and computer == "scissors") \
        or (you == "scissors" and computer == "lizard") or (you == "scissors" and computer == "paper") \
        or (you == "paper" and computer == "spock") or (you == "paper" and computer == "rock"):
            return True


retry = input("Play? [yes/no]: ")
while retry == "yes":
    print(game())
