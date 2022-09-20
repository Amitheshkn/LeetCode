class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        list_length=len(nums)
        if list_length==1:
            return nums[0]
        dp=[float('-inf')]*list_length
        dp[0]=nums[0]
        for i in range(1,list_length):
            if dp[i-1]>=0:
                dp[i]=dp[i-1]+nums[i]
            else:
                dp[i]=nums[i]
        return max(dp)
