# n, m, k = map(int, input().split())
# line = list(map(int, input().split()))

# line.sort()

# result = 0
# flag = 0
# index = -1
# for i in range(m):
#     if flag == k:
#         index = -2
#         flag = 0
#     result += line[index]
#     index = -1
#     flag += 1

# print(result)

n, m, k = map(int, input().split())
line = list(map(int, input().split()))

line.sort()
first = line[-1]
second = line[-2]

count = 0
result = 0

count += (m // (k + 1)) * k
count += m % (k + 1)

result += count * first
result += (m - count) * second

print(result)
