def main():
    time = float(input("Enter time in yrs: "))
    rate = float(input("Enter Rate for interest: "))
    princ = float(input("Enter the principal amt: "))
    inte = interest(time,rate,princ)
    print("The interest amount is:",inte)
    print("The amount is: ",inte+princ)

def interest(x,y,z):
    temp = x*y*z/100
    return temp

main()
