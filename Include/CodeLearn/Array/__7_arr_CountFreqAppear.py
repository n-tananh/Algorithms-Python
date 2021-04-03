def counting(arr):
    b = [0] * (max(arr) + 1)
    print("b" , b)

    for i in range(len(arr)):
        b[arr[i]] += 1
        print(b)

    for i in range(0, len(b)):
        if b[i] != 0:
            print(i, "-", b[i], end="; ")

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    counting(arr)
