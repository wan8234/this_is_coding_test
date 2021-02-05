# n = int(input())
# k = int(input())
# apple = [[0] * n for _ in range(n)]
# for i in range(k):
#     a, b = map(int, input().split())
#     apple[a - 1][b - 1] = 1
# l = int(input())
# times = []
# for roop in range(l):
#     times.append(list(input().split()))

# # right: 1, bottom: 2, left: 3, top: 4
# direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# snake = [[0] * n for _ in range(n)]
# snake[0][0] = 1
# head = [0, 0]
# tail = [0, 0]

# time = times[0]
# times = times[1:]
# roop = 0
# # for roop in range(1, int(times[-1][0]) + 1): #최대치만큼 반복
# while True:
#     roop += 1
#     face = snake[head[0]][head[1]] - 1
#     nextX = head[0] + direction[face][0]
#     nextY = head[1] + direction[face][1]
#     if nextX >= n or nextX < 0 or nextY >= n or nextY < 0: #범위 벗어남
        
#         break
#     elif snake[nextX][nextY] != 0: #몸통에 부딪힘
     
#         break

#     snake[nextX][nextY] = snake[head[0]][head[1]]
#     head = [nextX, nextY] 
#     if apple[nextX][nextY] != 1:
#         temp = tail
#         face = snake[tail[0]][tail[1]] - 1
#         nextXT = tail[0] + direction[face][0]
#         nextYT = tail[1] + direction[face][1]
#         tail = [nextXT, nextYT]
#         snake[temp[0]][temp[1]] = 0

#     if time != [] and int(time[0]) == roop:
#         temp = snake[nextX][nextY]
#         if time[1] == 'D':
#             temp += 1
#             if temp > 4:
#                 temp = 1
#         elif time[1] == 'L':
#             temp -= 1
#             if temp < 1:
#                 temp = 4
#         snake[nextX][nextY] = temp
#         if times != []:
#             time = times[0]
#             times = times[1:]
#     if times == []:
#         print('nothing')
# print(roop)
   
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x, y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
    return time
print(simulate())