def main():
    num = int(input("Enter a number"))
    if is_even(num):
        print("the number is Even")
    else:
        print("The number is odd")

def is_even(n):
    return n % 2 == 0 

main()




