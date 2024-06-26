import sys
import collections
input = lambda: sys.stdin.readline().rstrip()
II = lambda: int(input())
MII = lambda: map(int, input().split())
mod = 1000000007
mod2 = 998244353
tcn = II()
for _ in range(tcn):
    n = int(input())
    adj = [[] for _ in range(n)]
    values = list(map(int, input().split()))
    for _ in range(n - 1):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    minnd = values.index(min(values))
    visited = [False] * n
    order = [minnd]
    visited[minnd] = True
    bfs = collections.deque([minnd])
    while bfs:
        node = bfs.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                order.append(neighbor)
                bfs.append(neighbor)
    answer = order[1:][::-1]
    answer = [i + 1 for i in answer]
    print(len(answer))
    print(*answer)
