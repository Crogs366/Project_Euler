number = 1
circle = 1
count = 0
while count <= 500:
    circle += 1
    for i in range (1, number + 1):
        if number % i == 0:
            count += 1
    if count < 501:
        number += circle
        count = 0
print(number)