n = int(input())
queue = []
for i in range(n):
    queue.append(int(input()))

k = int(input())
for i in range(k):
    queue.append(queue.pop(0))
for x in queue:
    print(x,end=' ')

