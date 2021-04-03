import math

# Lỗi

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def isSupperPrime(n):
    queue = []
    if n <= 10:
        for a in range(1, n+1):
            if(isPrime(a)):
                queue.append(a)
                print(queue[0] , end= " ")
                queue.pop()
    else:
        for a in range(2, 10):
            if isPrime(a):
                queue.append(a)
            while not len(queue) == 0:
                for a in range(1, 10):
                    tmp = queue[0] * 10 + a
                    if isPrime(tmp) and tmp < n:
                        queue.append(tmp)

        print(queue)


if __name__ == '__main__':
    queue = []
    n = int(input())
    isSupperPrime(n)
