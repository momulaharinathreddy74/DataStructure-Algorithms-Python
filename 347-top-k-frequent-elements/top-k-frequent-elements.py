import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        heap=[]
        for num,fre in count.items():
            if len(heap)<k:
                heapq.heappush(heap,(fre,num))
            else:
                heapq.heappushpop(heap,(fre,num))
        return [num for _,num in heap]