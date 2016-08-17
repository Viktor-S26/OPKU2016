def generate_number():
     return lambda random_seed: (random_seed*693 + 5)%100
number = generate_number()

kol = 0
summa = 0
i = 1
while number(i) != 0:
    if number(i) % 4 == 0:
        kol += 1
        summa += number(i)
    i += 1

print(summa / kol)
