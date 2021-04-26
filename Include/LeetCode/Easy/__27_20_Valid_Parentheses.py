def isValid(s: str) -> bool:
    # stack = []
    # dict_s = {"]": "[", "}": "{", ")": "("}
    # for char in s:
    #     if char in dict_s.values():
    #         stack.append(char)
    #     elif char in dict_s.keys():
    #         if stack == [] or dict_s[char] != stack.pop():
    #             return False
    #     else:
    #         return False
    # return stack == []

    char = []
    dict_s = {"]": "[", "}": "{", ")": "("}
    for i in range(len(s)):
        if s[i] in dict_s.values():
            char.append(s[i])
        elif s[i] in dict_s.keys():
            if char == [] or dict_s[s[i]] != char.pop():
                return False
        else:
            return False
    return char == []

if __name__ == '__main__':
    s = "()"
    print(isValid(s))