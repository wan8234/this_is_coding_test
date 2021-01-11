# N, K = map(int, input().split())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

# A.sort()
# B.sort()

# A = A[K:] + B[len(B) - K:]
# print(sum(A))

N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(K):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else:
        break

print(sum(A))