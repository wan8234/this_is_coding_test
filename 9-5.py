import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())

graph = [[] for _ in range(N + 1)]

distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)

count = -1
max_value = 0

for dist in distance:
    if dist == INF:
        continue
    else:
        count += 1
        max_value = max(max_value, dist)

print(count, max_value)

# 입력 예시
# 3 2 1
# 1 2 4
# 1 3 2