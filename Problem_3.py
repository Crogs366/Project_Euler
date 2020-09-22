n = 600851475143
list = []
d = 2
while d * d <= n:
    if n % d == 0:
        list.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    list.append(n)
print(list[-1])