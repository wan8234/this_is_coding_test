n = int(input())
num = list(map(int, input().split()))
operator = list(map(int, input().split()))
operation = []

maximum = 0
minimum = 0
first = 0

def dfs(num, operator, operation):
    if sum(operator) == 0:
        calc(num, operation)
    else:
        for i in range(4):
            if operator[i] != 0:
                operator[i] -= 1
                operation.append(i)
                dfs(num, operator, operation)
                operator[i] += 1
                operation.pop()

def calc(num, operation):
    global maximum
    global minimum
    global first
    result = num[0]

    for i in range(len(operation)):
        if operation[i] == 0:
            result += num[i + 1]
        elif operation[i] == 1:
            result -= num[i + 1]
        elif operation[i] == 2:
            result *= num[i + 1]
        elif operation[i] == 3:
            if result < 0:
                result = -(result*(-1)//num[i + 1])
            else:
                result = result // num[i + 1]
    
    if first == 0:
        first = 1
        maximum = result
        minimum = result
    else:
        maximum = max(maximum, result)
        minimum = min(minimum, result)

dfs(num, operator, operation)
print(maximum)
print(minimum)