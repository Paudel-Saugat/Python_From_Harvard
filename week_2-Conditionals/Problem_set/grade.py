score = float(input("Enter your test score: "))

if score >= 90:
    print("Your grade is solid A")
elif score >=80 and score <90:
    print("Your grade is B")
elif score >=70 and score <80:
    print("Your grade is C")
elif score >=60 and score <70:
    print("Your grade is D")
elif score >=50 and score <60:
    print("Your grade is F")
else:
    print("You failed the test bro")