class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
    
        def rec(num):
            if num <= 2:
                return num

            if num in cache:
                return cache[num]
            
            result = rec(num-1) + rec(num-2)
            
            cache[num] = result
            
            return result
        return rec(n)
