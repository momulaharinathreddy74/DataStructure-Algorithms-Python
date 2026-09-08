class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dict1={}
        for num in answers:
            if num in dict1:
                dict1[num]+=1
            else:
                dict1[num]=1
        ans=0
        print(dict1)
        for key,val in dict1.items():
            if key==0:
                ans+=val
            elif val<=key:
                ans+=key+1
            else:
                nu=val//(key+1)
                rem=val%(key+1)
                if rem==0:
                    ans+=nu*(key+1)
                else:
                    ans+=(nu+1)*(key+1)
        return ans