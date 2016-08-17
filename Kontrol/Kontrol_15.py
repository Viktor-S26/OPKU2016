def generate_number():
     return lambda random_seed: (random_seed*693 + 5)%100
number = generate_number()

min = 100000000
i = 1

while number(i) != 0:
    if number(i) % 3 == 0 and number(i) < min:
        min = number(i)
    i += 1

print(min)
