num = int(input())

isPrime = [True] * (num + 1)

isPrime[1] = False

for i in range(2, num + 1):
    if isPrime[i]:
        for j in range(i * 2, num + 1, i):
            isPrime[j] = False

for i in range(1 , len(isPrime)):
    if isPrime[i]:
        print(i, end= " ")