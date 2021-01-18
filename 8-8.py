# N, M = map(int, input().split())
# coins = []
# for i in range(N):
#     coins.append(int(input()))

# dp = [-1] * 10001

# for coin in coins:
#     dp[coin] = 1

# for i in range(coins[0], M + 1):
#     mini = 0
#     for coin in coins:
#         temp = i - coin
#         if temp < 0:
#             continue
#         else:
#             if dp[temp] != -1:
#                 temp = dp[temp] + 1
#                 if mini == 0:
#                     mini = temp
#                 else:
#                     mini = min(mini, temp)
#                 dp[i] = mini

# print(dp[M])

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0

for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])