class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            swapped = False
            for j in range(len(nums)-i-1):
                if nums[j] == 0:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    swapped = True
            if not swapped:
                break