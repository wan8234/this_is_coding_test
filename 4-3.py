knight = input()

position = [int(knight[1]), int(ord(knight[0]) - ord('a')) + 1]

moves = [[-1, -2], [1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1]]

result = 0

for move in moves:
    if position[0] + move[0] < 1 or position[0] + move[0] > 8:
        continue
    elif position[1] + move[1] < 1 or position[1] + move[1] > 8:
        continue
    result += 1

print(result)