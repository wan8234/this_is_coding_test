from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x])

while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

flag = 0

for index in range(n + 1):
    if distance[index] == k:
        flag = 1
        print(index)
if flag == 0:
    print(-1)