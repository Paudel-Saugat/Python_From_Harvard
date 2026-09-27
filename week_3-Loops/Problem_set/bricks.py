def main():
   squ = int(input("Enter how many row and column"))
   make_square(squ)

def make_square(n):
    for i in range(n):
        for j in range(n):
            print("#", end = "")
        print("")


main()