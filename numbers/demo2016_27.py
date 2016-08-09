N = int(input())
# считываем в очередь первые 6 чисел

Q = [int(input()) for i in range(6)]
min_even = 1001
beta = 1000001
#pos = 0
for i in range(N-6):
    #первый элемент покидает очередь - и соревнуется с текущими минимальными
    x = Q[0]  #x = Q[pos%6]
    min_x = min(min_x, x)
    if x%2 == 0 and x < min_even:
        min_even = x
    x = int(input())
    beta = min(beta, x*min_even)
    if x%2 ==0:
        beta = min(beta, x*min_x)

    Q.pop(0)   #Q[pos%6] = x
    Q.append(x)  #pos +=1

    """
    for i in range(5):
        Q[i] = Q[i+1]
    Q[5] = x
    """
