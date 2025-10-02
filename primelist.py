# List the prime numbers within a range

l = int(input("\nLower limit: "))
u = int(input("\nUpper limit: "))

def check_prime(num):
    is_prime = True
    if num == 1 or num == 0:
        is_prime = False
    else:
        for i in range(2,num):
            if num % i == 0:
                is_prime = False
    return is_prime
       
for i in range(l,u+1):
    if check_prime(i) == True:
        print(i)
        

