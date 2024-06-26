import sys

input = lambda: sys.stdin.readline().rstrip()
I = lambda: input()
II = lambda: int(input())
MII = lambda: map(int, input().split())
LII = lambda: list(MII())
YN = lambda x: print('YES' if x else 'NO')
mod = 1000000007
mod2 = 998244353

t = int(input())
for _ in range(t):
    n = int(input())
    if n == 3:
        print("1 2 3")
    elif n % 2 == 0:
        for i in range(1, n // 2 + 1):
            print(f"{i} {n + 1 - i}", end=" ")
        print()
    else:
        for i in range(1, n // 2 + 1):
            print(f"{i} {n - i}", end=" ")
        print(n)
