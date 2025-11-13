n = int(input('Enter number of inputs: '))
line = input('Enter numbers: ').split()
num_list = []
for i in line:
    num_list.append(int(i))
while not all(i < 10 for i in num_list):  
    res = []  
    for i in num_list:
        num = i
        sum = 0
        while i > 0:
            m = i % 10
            sum += m
            i = i // 10
        res.append(sum)
    num_list = res
print(num_list)