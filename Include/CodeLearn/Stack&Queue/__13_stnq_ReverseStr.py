import Include.CodeLearn.ADTs.Stack as Stack


st = Stack.Stack()

str = input()
for i in range(len(str)):
    st.push(str[i])

ans = ""
while not st.isEmpty():
    ans += st.pop()
print(ans)