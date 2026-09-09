class Solution:
    def countCommas(self, n: int) -> int:
        nu=len(str(n))
        
        if nu<4:
            return 0
        ans=0
        if 4<=nu<7:
            nu1=min(n,999999)
            ans=nu1-1000+1
        elif 7<=nu<10:
            nu1=min(n,999999)
            fir=nu1-1000+1
            nu2=min(n,999999999)
            ans=(nu2-1000000+1)*2+fir
        elif 10<=nu<13:
            nu1=min(n,999999)
            fir=nu1-1000+1
            nu2=min(n,999999999)
            sec=(nu2-1000000+1)*2
            nu3=min(n,999999999999)
            ans=(nu3-1000000000+1)*3+fir+sec
        elif 13<=nu<=15:
            nu1=min(n,999999)
            fir=nu1-1000+1
            nu2=min(n,999999999)
            sec=(nu2-1000000+1)*2
            nu3=min(n,999999999999)
            thi=(nu3-1000000000+1)*3
            nu4=min(n,999999999999999)
            ans=(nu4-1000000000000+1)*4+fir+sec+thi
        elif nu==16:
            nu1=min(n,999999)
            fir=nu1-1000+1
            nu2=min(n,999999999)
            sec=(nu2-1000000+1)*2
            nu3=min(n,999999999999)
            thi=(nu3-1000000000+1)*3
            nu4=min(n,999999999999999)
            fou=(nu4-1000000000000+1)*4
            nu5=min(n,999999999999999999)
            ans=(nu5-1000000000000000+1)*5+fir+sec+thi+fou
        else:
            return 0
        return ans