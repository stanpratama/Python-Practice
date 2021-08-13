p1 = ''
p2 = ''
p1_score = 0
p2_score = 0

print("Rock Paper Scissors")
print("2 Players Game, Best 2 out of 3")

while True:
    # Determining The Winner and Replay the Game
    if p1_score == 2 or p2_score == 2:
        print("============FINAL RESULTS==========")
        if p1_score > p2_score:
            print("Player 1 Win The Game")
        elif p1_score < p2_score:
            print("Player 2 Win The Game")
        print("===================================")
        play = input("Do you want to play again?(yes/no) ").lower()
        if play[0] == "n":
            print("Thanks for playing")
            break
        else:
            p1_score = 0
            p2_score = 0

    # User Input
    p1 = input("Player 1 Choice: ").lower()
    while p1 != "paper" and p1 != "rock" and p1 != "scissors":
        p1 = input("Player 1, please correct your input: ").lower()
    print(".\n" * 100)
    p2 = input("Player 2 Choice: ").lower()
    while p2 != "paper" and p2 != "rock" and p2 != "scissors":
        p2 = input("Player 2, please correct your input: ").lower()

    # Game Mechanism
    print("==============RESULTS==============")
    if p1 == p2:
        print("It's a Draw")
    elif p1 == "rock" and p2 == "scissors":
        print("Player 1 win this round")
        p1_score += 1
    elif p1 == "paper" and p2 == "rock":
        print("Player 1 win this round")
        p1_score += 1
    elif p1 == "scissors" and p2 == "paper":
        print("Player 1 win this round")
        p1_score += 1
    else:
        print("Player 2 win this round")
        p2_score += 1
    print(f"Player 1 Score: {p1_score} | Player 2 Score: {p2_score}")
    print("===================================")
