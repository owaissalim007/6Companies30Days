class Solution:
    def getMoneyAmount(self, n: int) -> int:
        if n == 1:
            return 0
        start_idx = 1 if n % 2 == 0 else 2
        cands = [i for i in range(start_idx, n, 2)]
        cands_num = len(cands)
        dp = [[0] * cands_num for _ in range(cands_num)]
        
        for i in range(cands_num):
            dp[i][i] = cands[i]
        
        for i in range(cands_num - 2, -1, -1):
            for j in range(i + 1, cands_num):
                dp[i][j] = float('inf')
                for k in range(i, j + 1):
                    dp_left = dp[i][k-1] if k != i else 0
                    dp_right = dp[k+1][j] if k!=j else 0
                    dp[i][j] = min(dp[i][j], cands[k] + max(dp_left, dp_right))
        return dp[0][-1]
