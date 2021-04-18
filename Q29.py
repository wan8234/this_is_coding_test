import sys
input = sys.stdin.readline

n, c = map(int, input().split())
house = []

for _ in range(n):
    house.append(int(input()))

house.sort()
result = 0

def count_house(distance):
    count = 1
    current = house[0]
    for i in range(1, n):
        if house[i] >= current + distance:
            count += 1
            current = house[i]
    return count

start = 1
end = house[-1] - house[0]

while start <= end:
    mid = (start + end) // 2
    count = count_house(mid)
    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
