class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        result = [1] * nums_len

        prefix = 1
        for i in range(nums_len):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(nums_len-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result           
        
