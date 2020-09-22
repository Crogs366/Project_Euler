number = 0
max = 0
for i in range (1, 1000):
    for j in range(1, 1000):
        number = i * j
        number = str(number)
        if int(number) > max and number == number[::-1]:
            max = int(number)
print(max)