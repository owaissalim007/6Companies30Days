class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = curSum = 0
        ans = float('inf')
        for i in range(len(nums)):
            curSum += nums[i]
            while curSum >= target:
                ans = min(ans, i + 1 - left)
                curSum -= nums[left]
                left += 1
        
        if ans == float('inf'):
            return 0
        else:
            return ans
