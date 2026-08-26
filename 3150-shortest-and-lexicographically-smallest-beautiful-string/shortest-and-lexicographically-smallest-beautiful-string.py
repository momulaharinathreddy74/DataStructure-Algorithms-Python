class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l=0
        d={}
        res=''
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            while d.get('1',0)>k:
                d[s[l]]-=1
                l+=1
            if d.get('1')==k:
                while s[l]=='0':
                    l+=1
                
                if len(res)==0:
                    res=max(res,s[l:r+1])

                elif len(s[l:r+1])<len(res):
                    res=s[l:r+1]
                elif len(s[l:r+1])==len(res) and s[l:r+1]<res:
                    res=min(res,s[l:r+1])
        return res