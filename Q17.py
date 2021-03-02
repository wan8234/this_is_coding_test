import sys
import copy
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def virus(current, graph, cop, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            if graph[nx][ny] == 0 and cop[nx][ny] == 0:
                graph[nx][ny] = current
    return temp

for time in range(s):
    temp = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                temp = virus(graph[i][j], graph, temp, i, j)

    graph = copy.deepcopy(temp)
    print(graph)
print(graph[x-1][y-1])