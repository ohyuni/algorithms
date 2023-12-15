import sys

# N: 표의 크기, M: 합을 구해야 하는 횟수
N, M = map(int, input().split())
table = []
for _ in range(N):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    table.append(numbers)
test_cases = [map(int, sys.stdin.readline().rstrip().split()) for _ in range(M)]

# 구간 합 구하기
prefix_sum = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    prefix_sum[i][0] = table[i][0]
    for j in range(1, N):
        prefix_sum[i][j] = prefix_sum[i][j - 1] + table[i][j]

for i in range(1, N):
    for j in range(N):
        prefix_sum[i][j] = prefix_sum[i - 1][j] + prefix_sum[i][j]

# 테스트 케이스 합 구하기
for test_case in test_cases:
    x1, y1, x2, y2 = [z - 1 for z in test_case]

    if x1 == 0 and y1 == 0:
        result = prefix_sum[x2][y2]
    elif x1 == 0:
        result = prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1]
    elif y1 == 0:
        result = prefix_sum[x2][y2] - prefix_sum[x1 - 1][y2]
    else:
        result = (
            prefix_sum[x2][y2]
            - prefix_sum[x2][y1 - 1]
            - prefix_sum[x1 - 1][y2]
            + prefix_sum[x1 - 1][y1 - 1]
        )

    print(result)
