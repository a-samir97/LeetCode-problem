class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            while left < right and nums[mid] == nums[left] == nums[right]:
                left += 1
                right -= 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left] if nums[left] < nums[left-1] else nums[left-1]
