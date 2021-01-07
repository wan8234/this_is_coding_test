global N
global M
N, M = map(int, input().split())
global tray
global visit

tray = []
visit = [[0 for i in range(M)] for j in range(N)]

for i in range(N):
    tray.append(list(map(int, input().split())))

global result
result = 0

def ice(posx, posy):
    if posx == N or posy == M or posx < 0 or posy < 0:
        return 0
    if tray[posx][posy] == 1:
        return 0
    elif tray[posx][posy] == 0 and visit[posx][posy] == 1:
        return 0
    elif tray[posx][posy] == 0 and visit[posx][posy] == 0:
        visit[posx][posy] = 1
        ice(posx + 1, posy)
        ice(posx - 1, posy)
        ice(posx, posy + 1)
        ice(posx, posy - 1)
        return 1

for row in range(N):
    for col in range(M):
        value = ice(row, col)
        if value == 1:
            result += 1

print(result)

# 입력 예시1
# 4 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 0 0 0 0 0

# 입력 예시2
# 15 14
# 0 0 0 0 0 1 1 1 1 0 0 0 0 0
# 1 1 1 1 1 1 0 1 1 1 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 1 1 1 0
# 1 1 0 1 1 1 0 1 1 0 0 0 0 0
# 1 1 0 1 1 1 1 1 1 1 1 1 1 1
# 1 1 0 1 1 1 1 1 1 1 1 1 0 0
# 1 1 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 1 1 1
# 0 0 0 0 0 0 0 0 0 1 1 1 1 1
# 0 1 1 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 1 1 1 1 1 1 1 1 0 0 0
# 0 0 0 0 0 0 0 1 1 1 1 0 0 0
# 1 1 1 1 1 1 1 1 1 1 0 0 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1
# 1 1 1 0 0 0 1 1 1 1 1 1 1 1