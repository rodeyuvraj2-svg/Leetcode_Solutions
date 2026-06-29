class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums)-1
            
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                
                if sum == target:
                    closest = sum
                    return closest
                
                if abs(target - sum) < abs(target - closest):
                    closest = sum

                if sum > target:
                    right -= 1
                    
                else:
                    left += 1

        return closest