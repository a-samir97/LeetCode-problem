class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        left = 0
        right = max(arr)
        while left < right:
            mid = (left + right) // 2
            temp = [min(mid, num) for num in arr]
            if sum(temp) < target:
                left = mid + 1
            else:
                right = mid
        
        # check the sum for left and left - 1
        s1 = abs(target - sum([min(left - 1, num) for num in arr]))
        s2 = abs(target - sum([min(left, num) for num in arr]))
        return left - 1 if s1 <= s2 else left