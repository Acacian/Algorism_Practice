N = input()
M = input()
K = input()

def lcs():
    n = len(N)
    m = len(M)
    k = len(K)
    
    dp = [[[0] * (n+1) for _ in range(m + 1)] for _ in range(k + 1)]
    for i in range(1, k + 1):
        for j in range(1, m + 1):
            for l in range(1, n + 1):
                if K[i-1] == M[j-1] == N[l-1]:
                    dp[i][j][l] = dp[i-1][j-1][l-1] + 1
                else:
                    dp[i][j][l] = max(dp[i-1][j][l], dp[i][j-1][l], dp[i][j][l-1])
                    
    return dp[k][m][n]

print(lcs())