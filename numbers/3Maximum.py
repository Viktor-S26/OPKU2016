x = int(input())
if x > m1:
    m1, m2, m3 = x, m1, m2
elif x > m2:
    m2, m3 = x, m2
elif x > m3:
    m3 = x

