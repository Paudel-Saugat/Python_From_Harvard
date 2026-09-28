def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


def main():
    inte = get_int("What's x?")
    print(f"x is {inte}")

main()