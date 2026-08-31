# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur=head
        li=[]
        while cur:
            li.append(cur.val)
            cur=cur.next
        ans=[]
        for i in range(1,len(li)-1):
            if li[i-1]<li[i] and li[i]>li[i+1]:
                ans.append(i+1)
            elif li[i-1]>li[i] and li[i]<li[i+1]:
                ans.append(i+1)
        if len(ans)<2:
            return [-1,-1]
        min_=float('inf')
        
        for i in range(1,len(ans)):
            if ans[i]-ans[i-1]<min_:
                min_=ans[i]-ans[i-1]
        max_=ans[-1]-ans[0]  
        return [min_,max_]