class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        pr=[0]*(n+1)
        su=[0]*(n+1)
        pr[0]=nums[0]
        for i in range(1,n):
            pr[i]=max(pr[i-1],nums[i])
        su[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            su[i]=min(su[i+1],nums[i])
        for i in range(n):
            if pr[i]-su[i]<=k:
                return i
        return -1