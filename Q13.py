# n, m = map(int, input().split())
# table = []
# chicken = []
# house = []
# global result
# result = n**2

# for i in range(n):
#     table.append(list(map(int, input().split())))

# for i in range(n):
#     for j in range(n):
#         if table[i][j] == 1:
#             house.append([i, j])
#         elif table[i][j] == 2:
#             chicken.append([i, j])

# def check(chicken, house, count, real, index):
#     if count == m:
#         distance(house, real)
#     else:
#         for i in range(index, len(chicken)):
#             real.append(chicken[i])
#             check(chicken, house, count + 1, real, i + 1)
#             real.remove(chicken[i])

# def distance(house, real):
#     global result
#     value = 0
#     for home in house:
#         dist = n**2
#         for chi in real:
#             temp = abs(home[0] - chi[0]) + abs(home[1] - chi[1])
#             dist = min(dist, temp)
#         value += dist
#     result = min(value, result)

# for i in range(0, len(chicken) - m + 1):
#     check(chicken, house, 0, [], i)
# print(result)

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c))
        elif data[c] == 2:
            chicken.append((r, c))
candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result
result = 1e9

for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)