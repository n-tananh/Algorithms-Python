def romanToInt(s):
    romanDic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    res = romanDic[s[-1]]
    if len(s) > 1:
        for i in range(len(s) - 1, 0, -1):
            if romanDic[s[i]] <= romanDic[s[i - 1]]:
                res += romanDic[s[i - 1]]
            else:
                res -= romanDic[s[i - 1]]
        return res

    return res

if __name__ == '__main__':
    s = "III"
    print(romanToInt(s))