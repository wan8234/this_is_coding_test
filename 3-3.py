# n, m = map(int, input().split())
# card = []

# for i in range(n):
#     card.append(list(map(int, input().split())))
#     card[i].sort()

# maximum = card[0][0]
# for i in range(1, n):
#     maximum = max(maximum, card[i][0])
# print(maximum)


n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)

    result = max(min_value, result)

print(result)