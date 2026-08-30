class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=1:
            return n
        min_=[float('inf'),-1]
        max_=[float('-inf'),-1]
        for i in range(n):
            if nums[i]<min_[0]:
                min_[0]=nums[i]
                min_[1]=i
            if nums[i]>max_[0]:
                max_[0]=nums[i]
                max_[1]=i
        opt1=max(min_[1],max_[1])+1
        opt2=len(nums)-min(min_[1],max_[1])
        opt3=min(min_[1],max_[1])+1+n-max(min_[1],max_[1])
        return min(opt1,opt2,opt3)