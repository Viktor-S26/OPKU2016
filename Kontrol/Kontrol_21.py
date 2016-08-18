words = input().split()

N = len(words)
for pos in range(N-1):
    for i in range(pos+1, N):
        if words[i] < words[pos]:
            words[i], words[pos] = words[pos], words[i]

print(words[N//2])