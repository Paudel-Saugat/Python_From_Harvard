import random
def main():
    print("The choices are: Rock, Paper, Scissor")
    choic = input("Enter your choice: ")
    ret = det_winner(choic)
    if ret == "Player":
        print("You won")
    elif ret == "Computer":
        print("You lost")
    else:
        print("The game was a tie")

def det_winner(cho):
    temp = random.choice(["Rock","Paper","Scissor"])
    print("The Choice Of computer is:",temp)
    if cho == "Rock" and temp == "Scissor":
        return "Player"
    elif cho == "Paper" and temp == "Rock":
        return "Player"
    elif cho == "Scissor" and temp == "Paper":
        return "Player"
    elif cho == temp:
        return "Tie"
    else:
        return "Computer"
main()    
