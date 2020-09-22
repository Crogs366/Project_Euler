list_all = []
list_primes = []
p = 2
n = 2000000
for i in range(2, n):
    list_all.append(i)

for i in list_all:
    if i ** 2 > n:
        break
    if i == 0:
        continue
    else:
        p = list_all.index(i**2)
        for j in range(p, len(list_all), i):
            list_all[j] = 0
            
for i in list_all:
    if i != 0:
        list_primes.append(i)      
print(sum(list_primes))