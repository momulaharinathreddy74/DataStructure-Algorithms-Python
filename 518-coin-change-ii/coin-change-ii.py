class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # n=len(coins)
        # dp=[[-1]*(amount+1) for _ in range(n)]
        # def solver(ind,tar):
        #     if tar==0:
        #         return 1
        #     if ind==n:
        #         return 0
        #     if dp[ind][tar]!=-1:
        #         return dp[ind][tar]
        #     not_take=solver(ind+1,tar)
        #     take=0
        #     if coins[ind]<=tar:
        #         take=solver(ind,tar-coins[ind])
        #     dp[ind][tar]=take+not_take
        #     return dp[ind][tar] 
        # return solver(0,amount)
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0]=1
        for i in range(n-1,-1,-1):
            for j in range(1,amount+1):
                not_take=dp[i+1][j]
                take=0
                if coins[i]<=j:
                    take=dp[i][j-coins[i]]
                dp[i][j]=take+not_take
        return dp[0][amount]