def main():
    file()

def file():
    characters = ["Arjun", "Krishna", "Ram", "Karn", "Laxman"]
    while True:
        i = int(input("Choose a character: "))
        try:
            print(characters[i])
            if i < 0:
                raise IndexError
            break
        except IndexError:
            print("You entered wrong index")
        else:
            pass
main()