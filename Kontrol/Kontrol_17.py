my_list = [(lambda x:(x*296+2410)%4096)(i) for i in range(2000)]
print(my_list)
min_x1 = min_x2 = 1000000
kol_x1 = kol_x2 = 0

while my_list:
    x = my_list.pop()
    if x < min_x1:
        min_x2 = min_x1
        kol_x2 = kol_x1
        min_x1 = x
        kol_x1 = 1
    elif x == min_x1:
        kol_x1 += 1

    elif x < min_x2:
        min_x2 = x
        #kol_x2 = 1
    elif x == min_x2:
        kol_x2 += 1

print('Количество равных второму минимальному элементу -', kol_x2)
