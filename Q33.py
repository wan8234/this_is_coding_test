import sys
input = sys.stdin.readline

n = int(input())
schedule = []
for _ in range(n):
    schedule.append(list(map(int, input().split())))

price = [0] * (n + 1)
result = 0

for i in range(n):
    use = schedule[i][0]
    pay = schedule[i][1]
    date = i + use

    price[i] = max(result, price[i])
    result = price[i]
    nex = price[i] + pay

    if date > n:
        continue
    
    if price[date] < nex:
        price[date] = nex
    
print(max(price))