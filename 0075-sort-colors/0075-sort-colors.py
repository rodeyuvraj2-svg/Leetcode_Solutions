class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for i in range(len(nums)-1):
            left = i
            right = len(nums)-1

            while left < right:
                if nums[left] > nums[right]:
                    nums[right], nums[left] = nums[left], nums[right]
                right -=1