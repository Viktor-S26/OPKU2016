x = int(input())
n = 0
s = 0
p = 1
while x:
    digit = x%10
    n += 1
    s += digit
    p *= digit

    x //= 10

print('kolichestvo chifor', n)
print('summa chifor', s)
print('proizvedenie chifor', p)
print('srednee arifmeticheskoe', s/n)

