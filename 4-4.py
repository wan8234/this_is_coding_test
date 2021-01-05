row, column = map(int, input().split())
posx, posy, side = map(int, input().split())

ground = []
for i in range(row):
    ground.append(list(map(int, input().split())))

memo = [[0 for i in range(column)] for j in range(row)]

print(memo)
moves = [(0, -1), (-1, 0), (0, 1), (1, 0)]

result = 1
count = 0

while True:
    memo[posx][posy] = 1
    
    side -= 1
    if side < 0:
        side = 3
    count += 1
    nextPos = [posx + moves[side][0], posy + moves[side][1]]

    if ground[nextPos[0]][nextPos[1]] != 1 and memo[nextPos[0]][nextPos[1]] != 1:
        posx = nextPos[0]
        posy = nextPos[1]
        count = 0
        result += 1
    elif ground[nextPos[0]][nextPos[1]] == 1 or memo[nextPos[0]][nextPos[1]] == 1:
        if count == 4:
            temp = side
            side -= 2
            if side < 0:
                side += 4

            nextPos = [posx + moves[side][0], posy + moves[side][1]]

            if ground[nextPos[0]][nextPos[1]] != 1:
                posx = nextPos[0]
                posy = nextPos[1]
                side = temp
                count = 0
            else:          
                break
        else:
            continue
print(result)
    