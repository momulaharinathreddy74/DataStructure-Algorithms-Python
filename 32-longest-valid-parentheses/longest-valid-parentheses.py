class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ma=0
        st=[-1]
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                    st.pop()
                    if not st:
                        st.append(i)
                    else:
                        ma=max(ma,i-st[-1])
        return ma