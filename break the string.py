def solve(S):
    Z = [0] * len(S)
    n = len(S)
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            Z[i] = min(r - i + 1, Z[i - l])
        while i + Z[i] < n and S[Z[i]] == S[i + Z[i]]:
            Z[i] += 1
        if i + Z[i] - 1 > r:
            l, r = i, i + Z[i] - 1
    return Z

t = int(input())
for _ in range(t):
    S = input().strip()
    n = len(S)
    if n % 2 != 0:
        print(0)
        continue
    Z = solve(S)
    pst = []
    for i in range(n):
        if i <= Z[i]:
            pst.append(i)
    zrev = solve(S[::-1])
    rstart = []
    for i in range(n):
        if i <= zrev[i]:
            rstart.append(n - i - 1)
    s = set(rstart)
    ans = 0
    for i in pst:
        end = 2 * i
        size = (n - 1 - end + 1) // 2
        coord = (n - 1) - size
        if coord in s:
            ans += 1
    print(ans)
