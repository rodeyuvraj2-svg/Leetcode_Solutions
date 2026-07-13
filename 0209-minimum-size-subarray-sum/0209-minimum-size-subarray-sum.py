class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = high = sum = 0
        res = float('inf')

        while (high < len(nums)):
            sum = sum + nums[high]

            while (sum >= target):
                length = high - low + 1
                res = min(res, length)
                sum = sum - nums[low]
                low += 1
            
            high += 1
        
        return 0 if res == float('inf') else res