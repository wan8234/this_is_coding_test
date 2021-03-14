n, l, r = map(int, input().split())

earth = []
for _ in range(n):
    earth.append(list(map(int, input().split())))

visit = [[0] * n for i in range(n)]
pixel = []
count = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def open(x, y):
    global visit
    global pixel
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n:
            temp = abs(earth[x][y] - earth[nx][ny])
            if visit[nx][ny] == 0 and temp >= l and temp <= r:
                visit[nx][ny] = 1
                pixel.append([nx, ny])
                open(nx, ny)

def calc():
    global earth
    global visit
    global pixel
    global count

    while True:        
        total = 0
        for i in range(n):
            for j in range(n):
                open(i, j)
        if pixel == []:
            return
        
        for pix in pixel:
            total += earth[pix[0]][pix[1]]
        num = total // len(pixel)
        print(len(pixel), num, total)
        for pix in pixel:
            earth[pix[0]][pix[1]] = num

        count += 1
        visit = [[0] * n for i in range(n)]
        pixel = []

calc()
print(count)