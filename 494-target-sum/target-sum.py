class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=sum(nums)
        if abs(target)>n:
            return 0
        if (n+target)%2:
            return 0
        tar=(n+target)//2
        dp=[0]*(tar+1)
        dp[0]=1
        for num in nums:
            for s in range(tar,num-1,-1):
                dp[s]+=dp[s-num]
        return dp[tar]