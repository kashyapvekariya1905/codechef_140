def solve(N, A):
    used = [False] * (N + 1) 
    for i in range(N):
        for j in range(A[i], N + 1):
            if not used[j]:
                used[j] = True
                break
        else:
            return False 
    return True
T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    if solve(N, A):
        print("YES")
    else:
        print("NO")