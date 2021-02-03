# s = input()

# alpha = [0] * 26
# number = 0

# for single in s:
#     if ord(single) >= ord('A') and ord(single) <= ord('Z'):
#         alpha[ord(single) - ord('A')] += 1
#     elif ord(single) >= ord('0') and ord(single) <= ord('9'):
#         number += int(single)

# result = ''
# for index in range(len(alpha)):
#     if alpha[index] != 0:
#         for i in range(alpha[index]):
#             result += chr(index + ord('A'))

# result += str(number)
# print(result)

# 입력 예시1
# K1KA5CB7

# 입력 예시2
# AJKDLSI412K4JSJ9D

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))