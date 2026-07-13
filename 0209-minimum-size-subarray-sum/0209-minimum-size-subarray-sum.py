class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = sum = 0
        res = float('inf')

        for high in range(0,len(nums)):
            sum = sum + nums[high]

            while (sum >= target):
                res = min(res, (high - low + 1))
                sum = sum - nums[low]
                low += 1
        
        return 0 if res == float('inf') else res