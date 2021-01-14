# X = int(input())

# array = [0] * 30001

# for i in range(1, X + 1):
#     a = i * 5
#     b = i * 3
#     c = i * 2
#     d = i + 1

#     if array[a] == 0:
#         array[a] = array[i] + 1
#     else:
#         if array[i] + 1 < array[a]:
#             array[a] = array[i] + 1

#     if array[b] == 0:
#         array[b] = array[i] + 1
#     else:
#         if array[i] + 1 < array[b]:
#             array[b] = array[i] + 1

#     if array[c] == 0:
#         array[c] = array[i] + 1
#     else:
#         if array[i] + 1 < array[c]:
#             array[c] = array[i] + 1

#     if array[d] == 0:
#         array[d] = array[i] + 1
#     else:
#         if array[i] + 1 < array[d]:
#             array[d] = array[i] + 1

# print(array[X])

x = int(input())

d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1

    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)
    
print(d[x])