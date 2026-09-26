def main():
    yr = int(input("Enter a year: "))
    if is_leap(yr):
        print("The year is leap")
    else:
        print("The year isn't leap")

def is_leap(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False


main() 