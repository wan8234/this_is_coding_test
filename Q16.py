import copy
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
max_value = 0
dx = [0, 1, 0, -1] # 오른쪽, 아래, 왼쪽, 위
dy = [1, 0, -1, 0] # 오른쪽, 아래, 왼쪽, 위

for i in range(n):
    graph.append(list(map(int, input().split())))

def virus(graph, x, y):
    if graph[x][y] == 2:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx >= 0 and ny >= 0 and nx < n and ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 2
                    virus(graph, nx, ny)


def wall(start, count):
    if count == 3:
        research = copy.deepcopy(graph)
        for i in range(n):
            for j in range(m):
                virus(research, i, j)
        value = 0
        for i in range(n):
            for j in range(m):
                if research[i][j] == 0:
                    value += 1
        global max_value
        max_value = max(value, max_value)
    else:
        for i in range(start, n*m):
            nx = i // m
            ny = i % m
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                wall(i, count + 1)
                graph[nx][ny] = 0

wall(0, 0)
print(max_value)