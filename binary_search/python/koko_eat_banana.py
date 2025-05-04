class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:

            mid = (left + right) // 2
            s = sum([ceil(p/mid) for p in piles])
            if s > h:
                left = mid + 1
            else:
                right = mid

        return left