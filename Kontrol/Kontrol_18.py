my_list = [(lambda x:(x*87+12)%100)(i) for i in range(20)]
print(my_list)
x = my_list.pop()
kol = 1
while len(my_list) > 0:
    num = my_list.pop()
    if num < min_x:
        min_x = num
        kol = 1
    elif num == min_x:
        kol += 1
print('Количество равных минимальному элементу -', kol)
