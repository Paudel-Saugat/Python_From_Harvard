def main():
    game_guess()

def game_guess():
    i = 0
    for i in range(1,50):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBizz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Bizz")
        else:
            print("Number is:", i)

main()
        