def main():
    n = int(input("Enter the number of which you want to calculate the table of: "))
    mult_table(n)

def mult_table(x):
    for i in range(1,11):
        print(x, " *", i, "=", x*i)

main()