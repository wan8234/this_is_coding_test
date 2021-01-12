N = int(input())
store = list(map(int, input().split()))

M = int(input())
ask = list(map(int, input().split()))

store.sort()
ask.sort()

def binary_search(store, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if store[mid] == target:
            return 1
        elif store[mid] < target:
            start = mid + 1
        elif store[mid] > target:
            end = mid - 1
    return 0

for target in ask:
    value = binary_search(store, target, 0, N - 1)
    if value == 1:
        print("Yes", end = " ")
    else:
        print("No", end = " ")

# 입력 예시
# 5
# 8 3 7 9 2
# 3     
# 5 7 9