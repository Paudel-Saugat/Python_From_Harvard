import random
def main():
    num = random.randint(1,100)
    guess_no(num)

def guess_no(n):
    coun = 0
    guess = 0
    while guess != n:
        guess = int(input("Enter your guess: "))
        if guess > n:
            print("Think lower ")
            coun += 1
        elif guess < n:
            print("Think higher ")
            coun += 1
        else:
            print("Correct guess")
            coun += 1
    print("The number was:", n)
    print("Your number of tries were:", coun)

main()