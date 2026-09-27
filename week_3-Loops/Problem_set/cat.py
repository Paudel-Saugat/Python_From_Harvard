def main():
    num = get_number()
    cat_meow(num)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def cat_meow(n):
    for _ in range (n):
        print("Meow")

main()