# n = input()

# count = 0
# current = n[0]
# for i in range(1, len(n)):
#     if n[i] != current:
#         count += 1
#         current = n[i]
    
# if count % 2 == 0:
#     print(count // 2)
# else:
#     print(count // 2 + 1)

# 입력 예시
# 0001100

data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))