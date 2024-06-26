def count_ways(N, M, A, B):
    candy = [0] * M
    choco = [0] * M
    for a in A:
        candy[a % M] += 1
    for b in B:
        choco[b % M] += 1
    ways = 0
    for i in range(M):
        for j in range(M):
            if (i + j) % M == 0:
                ways += candy[i] * choco[j]
    return ways
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(count_ways(N, M, A, B))