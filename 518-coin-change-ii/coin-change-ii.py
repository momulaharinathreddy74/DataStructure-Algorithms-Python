class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[-1]*(amount+1) for _ in range(n)]
        def solver(ind,tar):
            if tar==0:
                return 1
            if ind==n:
                return 0
            if dp[ind][tar]!=-1:
                return dp[ind][tar]
            not_take=solver(ind+1,tar)
            take=0
            if coins[ind]<=tar:
                take=solver(ind,tar-coins[ind])
            dp[ind][tar]=take+not_take
            return dp[ind][tar] 
        return solver(0,amount)