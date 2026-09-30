class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        st=0
        res=[]
        for s in seq:
            if s=='(':
                st+=1
                if st%2==1:
                    res.append(0)
                else:
                    res.append(1)
            else:
                if st%2==1:
                    res.append(0)
                else:
                    res.append(1)
                st-=1
        return res