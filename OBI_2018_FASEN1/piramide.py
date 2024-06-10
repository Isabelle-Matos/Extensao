N = int(input())

# Criar duas matrizes nulas
m = [[0 for i in range(N+1)] for i in range(N+1)]
dp = [[0 for i in range(N+1)] for i in range(N+1)]

# Lê a entrada e armazena dentro da matriz
for i in range(1, N+1):
    linha = [int(x) for x in input().split()]
    for j in range(1, N+1):
        m[i][j] = linha[j-1]


for i in range(1, N+1):
    for j in range(i, N+1):
        for k in range(j, j-i, -1):
            dp[i][j] += m[i][k]
        if i > 1:
            dp[i][j] += min(dp[i-1][j], dp[i-1][j-1])
    
print(dp[N][N])