import math
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dict1={}
        # dict2={}
        # for st in s:
        #     if st in dict1:
        #         dict1[st]+=1
        #     else:
        #         dict1[st]=1
        # for st in t:
        #     if st in dict2:
        #         dict2[st]+=1
        #     else:
        #         dict2[st]=1
        # res=0
        
        # for st,va in dict2.items():
        #     a=dict1[st]
        #     b=va
        #     print(a,b)
        #     if a>b:
        #         res=res+(math.factorial(a)//(math.factorial(a-b)*math.factorial(b)))
        #         print(res)
        #     else:
        #         continue

        # return res
        n=len(t)
        dp={}
        def solver(i,j):
            if j==n:
                return 1
            if i==len(s):
                return 0
            if (i,j) in dp:
                return dp[(i,j)]
            notake=solver(i+1,j)
            take=0
            if s[i]==t[j]:
                take=solver(i+1,j+1)
            dp[(i,j)]=take+notake
            return dp[(i,j)]
        return solver(0,0)