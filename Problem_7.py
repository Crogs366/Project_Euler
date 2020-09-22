list = [2]
number = 2
while len(list) != 10001:
    number +=1
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        if number in list:
            continue
        else:   
            list.append(number)
    number +=1
print(list[10000])