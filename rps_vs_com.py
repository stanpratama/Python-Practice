import random

print("Basic Rock Paper Scissors Game Against Computer")
print("Best 2 out of 3")

comp = ''
p1 = ''
p1_score = 0
comp_score = 0

while True:
    # Computer Pick Mechanism
    comp = random.choice(["rock", "paper", "scissors"])

    # Determining the Winner and Replay Mechanism
    if p1_score == 2 or comp_score == 2:
        print("============FINAL RESULTS==========")
        if p1_score > comp_score:
            print("Player Win The Game")
        elif p1_score < comp_score:
            print("Computer Win The Game")
        print("===================================")
        play = input("Do you want to play again? (yes/no) ").lower()
        if play[0] == "n":
            print("Thanks for playing")
            break
        else:
            p1_score = 0
            comp_score = 0

    # User Input
    p1 = input("Please enter your choice: ").lower()
    while p1 != "paper" and p1 != "rock" and p1 != "scissors":
        p1 = input("Please correct your input: ").lower()

    # Game Mechanism
    print("==============RESULTS==============")
    print(f"Player ({p1}) vs Computer ({comp})")
    if p1 == comp:
        print("It's a Draw")
    elif p1 == "rock" and comp == "scissors":
        print("You win this round")
        p1_score += 1
    elif p1 == "paper" and comp == "rock":
        print("You win this round")
        p1_score += 1
    elif p1 == "scissors" and comp == "paper":
        print("You win this round")
        p1_score += 1
    else:
        print("Computer win this round")
        comp_score += 1
    print(f"Player 1 Score: {p1_score} | Computer Score: {comp_score}")
    print("===================================")
