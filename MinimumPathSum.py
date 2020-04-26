grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

dp = grid
print(dp)
if grid:
    for i in range(1,len(dp[0])):
        dp[0][i] += dp[0][i-1]
    print(dp)    
        
    for i in range(1,len(dp)):
        dp[i][0] += dp[i-1][0]
    print(dp)    

    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j] += dp[i-1][j]
                
            else:
                dp[i][j] += dp[i][j-1]
    print(dp)
print(dp[-1][-1])