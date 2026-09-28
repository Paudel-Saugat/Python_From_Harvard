def main():
    r = safe_calc()
    print("Your result is:", r)

def safe_calc():
    while True:
        try:
            a = float(input("Enter first no: "))
            b = float(input("Enter second no: "))
            break
        except ValueError:
            print("Your input is invalid")
    
    oper = input("Ener the operation you want to perform i.e: add, sub, mul, divi; ")
    if oper == "add":
        return a+b
    elif oper == "sub":
        return a-b
    elif oper == "mul":
        return a*b
    elif oper == "divi":
        while True:
            try:
                return a/b
                break
            except ZeroDivisionError:
                print("The division is not possible")
                return None
      
    else:
        print("Invalid syntax input")
    
    


main()
        
        