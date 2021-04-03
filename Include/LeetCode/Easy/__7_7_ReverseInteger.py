# Python Slice Notation
# int(str(abs(x))[::-1])
# <object_name>[<start_index>, <stop_index>, <step>]

def reverseInt(x):
    sign = [1, -1][x < 0]
    ans = sign * int(str(abs(x))[::-1])
    return ans if -(2**31)-1 < ans < 2**31 else 0

def reverse_1(x):
    sign = [1, -1][x < 0]
    x = abs(x)
    ans = ''
    if x == 0:
        return 0
    while x > 0:
        tail = x % 10
        ans += str(tail)
        x //= 10
    res = sign * int(ans)
    return res if -(2 ** 31) - 1 < res < 2 ** 31 else 0

if __name__ == '__main__':
    x = int(input())
    print(reverseInt(x))