# def change(N):
#     coin = 0
    
#     coin += N // 500
#     N = N % 500
#     coin += N // 100
#     N = N % 100
#     coin += N // 50
#     N = N % 50
#     coin += N // 10
#     N = N % 10

#     return coin

# print(change(1260))

N = int(input())
count = 0

coins = [500, 100, 50, 10]

for coin in coins:
    count += N // coin
    N %= coin

print(count)