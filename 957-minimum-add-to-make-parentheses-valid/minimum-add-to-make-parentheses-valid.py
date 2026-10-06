class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        os=0
        cs=0
        for st in s:
            if st=='(':
                os+=1   
            else:
                if os==0:
                    cs+=1
                else:
                    os-=1
        return os+cs
       
        return abs(os-cs)