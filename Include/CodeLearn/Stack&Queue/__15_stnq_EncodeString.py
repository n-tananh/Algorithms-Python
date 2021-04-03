import Include.CodeLearn.ADTs.Stack as Stack

st = Stack.Stack()
s = input()
ans = ""


for i in range(len(s)):

    st.push(s[i])
    count = 0

    if i == len(s) - 1:
        ans += st.top()
        while not st.isEmpty():
            st.pop()
            count += 1
        ans += str(count)

    elif st.top() != s[i + 1]:
        ans += st.top()
        while not st.isEmpty():
            st.pop()
            count += 1
        ans += str(count)

print(ans)





