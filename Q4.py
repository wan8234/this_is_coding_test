# n = int(input())
# coins = list(map(int, input().split()))
# coins.sort(reverse=True)

# result = 0

# for value in range(1, sum(coins)):
#     temp = value
#     for coin in coins:
#         value -= coin
#         if value < 0:
#             value += coin
#         elif value > 0:
#             continue
#         elif value == 0:
#             break
    
#     if value != 0:
#         result = temp
#         break

# if result == 0:
#     print(sum(coins) + 4)
# else:
#     print(result)

# 입력 예시1
# 5
# 3 2 1 1 9

n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for coin in coins:
    if target < coin:
        break
    target += coin

print(target)