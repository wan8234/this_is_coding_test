n, m = map(int, input().split())
balls = list(map(int, input().split()))

balls.sort()
num = 0
result = 0

while balls[num] != m:
    temp = balls.count(balls[num])
    num += temp
    result += (n - num)*temp

print(result)

# 입력 예시1
# 5 3
# 1 3 2 3 2

# 입력 예시2
# 8 5
# 1 5 4 3 2 4 5 2

#교재 정답
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11
for x in data:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n
print(result)