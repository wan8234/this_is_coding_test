n = int(input())
array = set(map(int, input().split()))
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('Yes', end = ' ')
    else:
        print('No', end = ' ')

# 입력 예시
# 5
# 8 3 7 9 2
# 3     
# 5 7 9