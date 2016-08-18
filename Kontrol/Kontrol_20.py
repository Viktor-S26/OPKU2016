def pseudo_list():
    for i in range(N):
        yield (i*9876+1024)%1000
N = 10**6 + 1
A = pseudo_list()

count =[0] * 1000
for x in A:
    count[x] += 1

x = 0
summa = count[0]
while summa <= N//2:
    x += 1
    summa += count[x]

print(x)
