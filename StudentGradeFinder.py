# Python program to find the grade of a student

print("\nWelcome to STUDENT GRADE FINDER\n*******************************\n Enter your marks\n")
mark1 = int(input("Subject 1: \t"))
mark2 = int(input("Subject 2: \t"))
mark3 = int(input("Subject 3: \t"))
mark4 = int(input("Subject 4: \t"))
mark5 = int(input("Subject 5: \t"))

total = mark1 + mark2 + mark3 + mark4 + mark5

percentage = (total / 500) * 100

print("\n Your total marks is", total, " and you've got ",percentage,"%\n")

if percentage >= 90 and  percentage<=100:
    print("Congratulations!!! You have A+\n")
elif percentage >= 80 and percentage < 90:
    print("You have A grade\n")
elif percentage >= 70 and percentage < 80:
    print("You have B grade\n")
elif percentage >= 60 and percentage < 70:
    print("You have C grade\n")
elif percentage >= 50 and percentage > 60:
    print("You have D grade\n")
else:

    print("Oops..! You have F grade\n")
