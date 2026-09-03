class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        ev=0
        od=0
        for num in nums1:
            if num%2==0:
                ev+=1
            else:
                od+=1
        if ev==0 or od==0:
            return True
        
        else:
            nums1.sort()
            if nums1[0]%2==0:
                return False
            
        return True
           