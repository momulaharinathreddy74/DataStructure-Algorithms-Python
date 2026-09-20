class Solution:
    def reverseDegree(self, s: str) -> int:
        su=0
        for i in range(len(s)):
            val=ord('z')-ord(s[i])
            print(val)
            su+=(val+1)*(i+1)
        return su