class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for each_num in nums_set:
            if (each_num-1) not in nums_set:
                length = 0
                while (each_num + length) in nums_set:
                    length += 1

                longest = max(longest, length)

        return longest    
