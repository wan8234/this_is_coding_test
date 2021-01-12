def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("Doesn't exist")
else:
    print(result + 1)

# 입력 예시1
# 10 7
# 1 3 5 7 9 11 13 15 17 19

# 입력 예시2
# 10 7
# 1 3 5 6 9 11 13 15 17 19
