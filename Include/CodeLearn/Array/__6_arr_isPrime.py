import math
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())

    arr = [int(input()) for i in range(n)]

    for i in arr:
        if isPrime(i):
            print(i, end= " ")