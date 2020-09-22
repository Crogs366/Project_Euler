number = 20
count = 1
count_max = 0
while count_max != 20:
    for i in range(1, 21):
        if number % i == 0:
            count_max +=1
            if count_max == 20:
                print(number)
                break
        else:
            count_max = 0
            break
    number += 20 