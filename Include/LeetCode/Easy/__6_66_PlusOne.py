

# strNum = ''
# for num in digits:
#     strNum += str(num)
#
# asnNum = int(strNum) + 1
# result = [int(d) for d in str(asnNum)]

def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):

        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    newDigits = [0] * (len(digits) + 1)
    newDigits[0] = 1
    return newDigits

if __name__ == '__main__':

    digits = list(map(int, input().split()))
    print(plusOne(digits))