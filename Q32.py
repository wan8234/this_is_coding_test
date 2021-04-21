n = int(input())

pyramid = []
for _ in range(n):
    pyramid.append(list(map(int, input().split())))

graph = [[0] * n for _ in range(n)]

graph[0][0] = pyramid[0][0]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            graph[i][j] = pyramid[i][j] + graph[i - 1][j]
        elif j == i:
            graph[i][j] = pyramid[i][j] + graph[i - 1][j - 1]
        else:
            graph[i][j] = pyramid[i][j] + max(graph[i - 1][j], graph[i - 1][j - 1])

result = 0
for i in range(n):
    result = max(graph[n - 1][i], result)

print(result)