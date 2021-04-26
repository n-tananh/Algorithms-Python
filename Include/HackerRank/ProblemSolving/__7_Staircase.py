def staircase(n):
    for m in range(n):
        print((n - m - 1) * ' ' + (m + 1) * '#')

if __name__ == '__main__':
    n = 4
    staircase(n)