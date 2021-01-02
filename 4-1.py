N = int(input())
moves = list(input().split())

current = [1, 1]

for move in moves:
    if move == 'L':
        current[1] -= 1
        if current[1] < 1:
            current[1] = 1
    elif move == 'R':
        current[1] += 1
        if current[1] > 4:
            current[1] = 4
    elif move == 'U':
        current[0] -= 1
        if current[0] < 1:
            current[0] = 1
    elif move == 'D':
        current[0] += 1
        if current[0] > 4:
            current[0] = 1

print(current[0], current[1])