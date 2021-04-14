########## my solution ##########

n, x = map(int, input().split())

array = list(map(int, input().split()))

left = 0
right = n - 1

def binary_first(array, start, end):
    global left
    mid = (start + end) // 2
    if start > end:
        left = end
        return
    if array[mid] < x:
        binary_first(array, mid + 1, end)
    else:
        binary_first(array, start, mid - 1)

def binary_second(array, start, end):
    global right
    mid = (start + end) // 2
    if start > end:
        right = end
        return
    if array[mid] <= x:
        binary_second(array, mid + 1, end)
    else:
        binary_second(array, start, mid - 1)

binary_first(array, 0, n - 1)
binary_second(array, 0, n - 1)

print(right - left)


########## 1st solution ##########

def count_by_value(array, x):
    n = len(array)
    a = first(array, x, 0, n - 1)
    if a == None:
        return 0
    b = last(array, x, 0, n - 1)

    return b - a + 1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)


########## 2nd solution ##########

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)

if count == 0:
    print(-1)
else:
    print(count)