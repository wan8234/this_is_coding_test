n = int(input())
array = [0] * 1000001

for i in input().split():
    array[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('Yes', end = ' ')
    else:
        print('No', end = ' ')

# 입력 예시
# 5
# 8 3 7 9 2
# 3     
# 5 7 9