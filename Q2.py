s = input()

result = int(s[0])

for i in range(1, len(s)):
    if int(s[i]) < 2 or result < 2:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)

# 입력 예시1
# 02984

# 입력 예시2
# 567