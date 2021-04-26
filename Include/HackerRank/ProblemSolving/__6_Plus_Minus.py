def plusMinus(arr):
    p_numbers = 0
    n_numbers = 0
    z_numbers = 0

    for i in range(len(arr)):
        if arr[i] > 0:
            p_numbers += 1
        elif arr[i] < 0:
            n_numbers +=1
        elif arr[i] == 0:
            z_numbers += 1

    p = p_numbers / len(arr)
    n = n_numbers / len(arr)
    z = z_numbers / len(arr)

    print(f"{p:.6f}")
    print(f"{n:.6f}")
    print(f"{z:.6f}")
    
if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
