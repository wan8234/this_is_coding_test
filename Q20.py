n = int(input())

graph = []
cctv = 0
result = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(n):
    graph.append(list(input().split()))

def watch(room):
    global cctv
    for i in range(n):
        for j in range(n):
            if room[i][j] == 'T':
                for k in range(4):
                    nx = i
                    ny = j
                    while True:
                        nx = nx + dx[k]
                        ny = ny + dy[k]
                        if nx >= 0 and ny >= 0 and nx < n and ny < n:
                            if room[nx][ny] == 'S':
                                cctv = 1
                                break
                            elif room[nx][ny] == 'O':
                                break
                        else:
                            break
                    if cctv == 1:
                        return

def obstacle(start, count):
    global graph
    global result
    global cctv

    if result == 1:
        return
    if count < 3:
        for i in range(start, n*n):
            x = i // n
            y = i % n
            if graph[x][y] == 'X':
                graph[x][y] = 'O'
                obstacle(i, count + 1)
                graph[x][y] = 'X'
    elif count == 3:
        watch(graph)
        if cctv == 0:
            result = 1
            return
        cctv = 0

obstacle(0, 0)
if result == 0:
    print("NO")
else:
    print("YES")
