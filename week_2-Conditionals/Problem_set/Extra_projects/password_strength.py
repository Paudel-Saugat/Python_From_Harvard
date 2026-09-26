def main():
    pwd = input("Enter Your Password")
    res = check_strength(pwd)
    print("The strength of password is:",res)

def check_strength(temp):
    if len(temp) < 8:
        return "Weak"
    elif len(temp) >= 8 and len(temp) < 12:
        return "Moderate"
    elif len(temp) >= 12:
        return "Strong"
    

main()