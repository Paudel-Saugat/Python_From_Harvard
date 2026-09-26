def main():
    wt = float(input("Enter Your wt; "))
    ht = float(input("Enter your height in meters: "))
    val = bmi(wt,ht)
    print("Your BMI value is: ",val)

def bmi(x,y):
    temp = x/(y*y)
    return temp

main()
