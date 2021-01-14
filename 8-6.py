N = int(input())
K = list(map(int, input().split()))

array = [0] * N

array[0] = K[0]
# if K[0] > K[1]:
#     array[1] = K[0]
# else:
#     array[1] = K[1]

array[1] = max(K[0], K[1])

for i in range(2, N):
    array[i] = max(array[i - 1], array[i - 2] + K[i])

print(array[N - 1])