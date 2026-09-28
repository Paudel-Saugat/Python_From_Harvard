def main():
    res = real_age()
    print("Your age is:",res)

def real_age():
    while True:
        age = int(input("input age: "))
        try:
            if age < 0 or age > 100:
                raise ValueError
            return age
        except ValueError:
            print("your age isn't appropriate ")

main()

            
