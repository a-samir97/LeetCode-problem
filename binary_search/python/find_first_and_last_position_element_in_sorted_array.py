from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        start, end = -1, -1
        while left <= right:
            if nums[mid] == target:
                start = mid
                end = mid
                break
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1 
            mid = (left + right) // 2

        while start-1 >= 0 and nums[start-1] == target:
            start -= 1

        while end+1 <= len(nums)-1 and nums[end+1] == target:
            end += 1

        return [start, end]
