from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        start, end = 0, n-1

        while start + 1 < n and arr[start] <= arr[start + 1]:
            start += 1

        if start == n - 1:
            return 0

        while end > 0 and arr[end-1] <= arr[end]:
            end -= 1

        result = min(n - start - 1, end)

        i, j = 0, end

        while i <= start and j < n:
            if arr[i] <= arr[j]:
                result = min(result, j-i-1)
                i += 1
            else:
                j += 1

        return result
