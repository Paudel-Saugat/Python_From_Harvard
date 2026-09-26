def main():
    tp_amt = float(input("Enter the tip amount "))
    tp_per = float(input("Enter the tip percentage "))
    amt = calculate(tp_amt,tp_per)
    print("The tip amount is: ",amt)

def calculate(x,y):
    temp = x*y/100
    return temp

main()