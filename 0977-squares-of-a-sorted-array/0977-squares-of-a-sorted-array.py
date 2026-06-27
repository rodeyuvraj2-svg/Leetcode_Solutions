class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_nums = [0] * n  
        left, right = 0, n - 1
        pos = n-1

        while left <= right:
            l_s = nums[left] ** 2
            r_s = nums[right] ** 2
            
            if l_s > r_s:
                new_nums[pos] = l_s
                left += 1
            else:
                new_nums[pos] = r_s
                right -= 1
            pos -= 1

        return new_nums