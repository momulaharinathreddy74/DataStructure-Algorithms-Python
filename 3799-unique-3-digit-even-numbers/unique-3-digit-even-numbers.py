class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        seen=set()
        n=len(digits)
        for h in range(n):
            if digits[h]==0:
                continue
            for t in range(n):
                if t==h:
                    continue
                
                for u in range(n):
                    if u==h or u==t:
                        continue
                    if digits[u]%2==0:
                        nu=digits[h]*100+digits[t]*10+digits[u]*1
                        if nu not in seen:
                            seen.add(nu)
        return len(seen)