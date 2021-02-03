n = input()

length = len(n)
half = length // 2

front = 0
rear = 0

for i in range(half):
    front += int(n[i])

for i in range(half, length):
    rear += int(n[i])

if front == rear:
    print('LUCKY')
else:
    print('READY')