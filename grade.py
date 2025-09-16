# Calculate the grade of a student

sub1 = 78
sub2 = 85
sub3 = 92
sub4 = 74
sub5 = 88

total = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total / 500) * 100

print("\nTotal marks:\t",total,"\nPercentage:\t",percentage)

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