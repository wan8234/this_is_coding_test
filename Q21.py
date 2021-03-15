# n, l, r = map(int, input().split())

# earth = []
# for _ in range(n):
#     earth.append(list(map(int, input().split())))

# visit = [[0] * n for i in range(n)]
# pixel = []
# count = 0

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# def open(x, y):
#     global visit
#     global pixel
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 and ny >= 0 and nx < n and ny < n:
#             temp = abs(earth[x][y] - earth[nx][ny])
#             if visit[nx][ny] == 0 and temp >= l and temp <= r:
#                 visit[nx][ny] = 1
#                 pixel.append([nx, ny])
#                 open(nx, ny)
    

# def calc():
#     global earth
#     global visit
#     global pixel
#     global count

#     while True:        
#         total = 0
#         for i in range(n):
#             for j in range(n):
#                 open(i, j)

#                 if pixel != []:
#                     break
#             if pixel != []:
#                 break
#         if pixel == []:
#             return
        
#         for pix in pixel:
#             total += earth[pix[0]][pix[1]]
#         num = total // len(pixel)
#         #print(len(pixel), num, total)
#         for pix in pixel:
#             earth[pix[0]][pix[1]] = num

#         count += 1
#         #visit = [[0] * n for i in range(n)]
#         pixel = []

# calc()
# print(count)

from collections import deque

n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

result = 0

def process(x, y, index):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        graph[i][j] = summary // count
    return count

total_count = 0

while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i, j, index)
                index += 1
    if index == n * n:
        break
    total_count += 1
print(total_count)
