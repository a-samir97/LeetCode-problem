from typing import List

# Time complexity: O(n^2)
# Space complexity: O(n)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        s = set()
        for i in range(1, len(nums)):
            left = 0
            right = len(nums) - 1

            while i > left and right > i:
                current_target = nums[i] + nums[left] + nums[right]
                if current_target == 0 and (nums[i], nums[left], nums[right]) not in s:
                    result.append([nums[i], nums[left], nums[right]])
                    s.add((nums[i], nums[left], nums[right]))
                    right -= 1
                    left += 1
                elif current_target > 0:
                    right -= 1
                else:
                    left += 1
        return result
