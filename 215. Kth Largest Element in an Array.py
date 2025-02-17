#space: O(k)
#Time: O(n)
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq= []
        for n in nums:
            heapq.heappush(pq, n)
            if len(pq) >k:
                heapq.heappop(pq)
        
        return heapq.heappop(pq)   
