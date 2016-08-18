my_list = [(lambda x:(x*87+12)%100)(i) for i in range(20)]
print(my_list)

summa = 0
summa_kvadrat = 0

kol = 0
while len(my_list) > 0:
    x = my_list.pop()
    if x % 2 == 0:
        summa += x
        summa_kvadrat += x*x
        kol +=1

srednee = summa / kol
srednee_kvadrat = summa_kvadrat / kol
otklonenie = (srednee_kvadrat - srednee ** 2)** 0.5

print(otklonenie)
