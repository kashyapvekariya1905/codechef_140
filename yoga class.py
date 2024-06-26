def max_earnings(N, X, Y):
    if Y > 2*X:
        a = N // 2
        hrs = N % 2
        return a * Y + hrs * X
    else:
        return N * X

T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    print(max_earnings(N, X, Y))