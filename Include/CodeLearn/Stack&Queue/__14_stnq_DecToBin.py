import Include.CodeLearn.ADTs.Stack as Stack

s1= Stack.Stack()
decNum= int(input("Enter the decimal num : "))
while decNum!=0:
    newNum= decNum%2
    decNum = decNum//2
    s1.push(newNum)

while not s1.isEmpty():
    a = s1.pop()
    print(str(a), end= '')
