class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = high = sum = 0
        res = float('inf')

        for high in range(len(nums)):
            sum += nums[high]

            while sum >= target:
                res = min(res, high-low+1)
                sum -= nums[low]
                low += 1
        
        return 0 if res == float('inf') else res