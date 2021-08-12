n = int(input())
consult = []

for _ in range(n):
    consult.append(list(map(int, input().split())))

result = [0] * (n + 1)
maximum = 0

for i in range(n):
    day = consult[i][0]
    pay = consult[i][1]

    date = i + day

    result[i] = max(maximum, result[i])
    maximum = result[i]
    over = maximum + pay

    if date > n:
        continue

    if over > result[date]:
        result[date] = over


print(max(result))



