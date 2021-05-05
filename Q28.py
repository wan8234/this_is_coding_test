n = int(input())
a = list(map(int, input().split()))

result = -1

def binary(start, end):
    global result
    mid = (start + end) // 2
    if start > end:
        return
    
    if mid == a[mid]:
        result = mid
    elif mid > a[mid]:
        binary(mid + 1, end)
    elif mid < a[mid]:
        binary(start, mid - 1)


binary(0, n - 1)
print(result)