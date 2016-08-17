def generate_number():
     return lambda random_seed: (random_seed*693 + 5)%100
number = generate_number()

s = 0
i = 1
while number(i) != 0:
    if number(i) % 7 == 0:
        s += number(i)
    i += 1

print(s)
