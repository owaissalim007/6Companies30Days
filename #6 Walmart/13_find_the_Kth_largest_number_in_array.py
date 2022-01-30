class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        minheap = []
        heapq.heapify(minheap)
        for i in range(0, len(nums)):
            heapq.heappush(minheap, int(nums[i]))
            if len(minheap) > k:
                heapq.heappop(minheap)
        return str(heapq.heappop(minheap))
