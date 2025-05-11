class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            skip = dp[i-1]
            take = dp[i-2] + nums[i-1]
            dp[i] = max(skip, take)
        
        return dp[len(nums)]
