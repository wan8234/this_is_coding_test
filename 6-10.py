count = int(input())
result = []
for i in range(count):
    result.append(int(input()))

result = sorted(result, reverse=True)

for i in result:
    print(i, end = ' ')