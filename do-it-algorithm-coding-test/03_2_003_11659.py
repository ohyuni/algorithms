import sys

N, M = map(int, input().split())
arr = list(map(int, input().split()))
test_cases = [sys.stdin.readline().rstrip() for _ in range(M)]

# 구간 합 구하기
prefix_sum = [0 for i in range(N)]
prefix_sum[0] = arr[0]
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]

for test_case in test_cases:
    i, j = map(int, test_case.split())
    i -= 1
    j -= 1
    if i == 0:
        print(prefix_sum[j])
    else:
        print(prefix_sum[j] - prefix_sum[i - 1])
