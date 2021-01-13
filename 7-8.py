N, M = map(int, input().split())
rices = list(map(int, input().split()))

start = 0
end = max(rices)

def binary_search(rices, M, start, end):
    while start <= end:
        mid = (start + end) // 2
        result = 0
        for rice in rices:
            temp = rice - mid
            if temp > 0:
                result += temp
        
        if result == M:
            return mid
        elif result > M:
            start = mid + 1
        elif result < M:
            end = mid - 1

print(binary_search(rices, M, start, end))

# 입력 예시
# 4 6
# 19 15 10 17