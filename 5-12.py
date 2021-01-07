from collections import deque

N, M = map(int, input().split())
maze = []
for i in range(N):
    maze.append(list(map(int, input().split())))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def escape(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for move in moves:
            nx = x + move[0]
            ny = y + move[1]

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if maze[nx][ny] == 0:
                continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    
    return maze[N - 1][M - 1]

print(escape(0, 0))

# 입력 예시1
# 5 6
# 1 0 1 0 1 0
# 1 1 1 1 1 1
# 0 0 0 0 0 1
# 1 1 1 1 1 1
# 1 1 1 1 1 1