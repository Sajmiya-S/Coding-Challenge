# Check whether the given number is Armstrong number or not

def check_armstrong(num):
    count = 0
    n = num
    result = 0
    while num != 0:
        m = num % 10
        count += 1
        num = num // 10
    num = n
    while n != 0:
        for i in range(count):
            m = n % 10
            result += m ** count
            n = n // 10
    if num == result:
        return True
    else:
        return False
        
    
n = int(input("Enter a number: "))

if check_armstrong(n) == True:
    print("Armstrong number")
else:
    print("Not Armstrong number")

# Print all Armstrong numbers in a given range

r = int(input("Enter the upper limit to find Armstrong number within a range: "))

for i in range(r):
    if check_armstrong(i) == True:
        print(i, end = ' ')