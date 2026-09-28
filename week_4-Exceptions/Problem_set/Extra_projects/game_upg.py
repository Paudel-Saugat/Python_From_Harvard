import random
def main():
    n = random.randint(1,200)
    random_game(n)

def random_game(a):
    cnt = 0
    guess = 0
    while guess != a:
        
        try:
            guess = int(input("Enter a number between 1 and 200:"))
            if guess < 0 or guess > 200:
                raise ValueError
            if guess > a:
                print("Guess Lowwe")
                cnt += 1
            elif guess < a:
                print("Guess Higher")
                cnt += 1
            else:
                print("Correct Guess")
                cnt += 1
        except ValueError:
            print("You entered wrong, Try again")
    print("The random number was:", a)
    print("Your number of tries are: ", cnt)


main()