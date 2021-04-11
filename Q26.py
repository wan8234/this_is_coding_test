import heapq

n = int(input())
card = []
for _ in range(n):
    heapq.heappush(card, int(input()))

result = 0

while len(card) != 1:
    one = heapq.heappop(card)
    two = heapq.heappop(card)
    temp = one + two
    result += temp
    heapq.heappush(card, temp)

print(result)