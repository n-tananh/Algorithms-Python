def reverseString(s) -> None:
    i = 0
    j = len(s) - 1

    while i < j:
        tmp = s[i]
        s[i] = s[j]
        s[j] = tmp
        i += 1
        j -= 1

if __name__ == '__main__':
    s = ["H", "a", "n", "n", "a", "h"]
    s2 = ["T", "a", "n", "A", "n", "h"]

    print(s2)
    reverseString(s2)
    print(s2)