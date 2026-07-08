class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            left = i + 1
            if nums[i] == nums[left]:
                return nums[i]
            else:
                continue
