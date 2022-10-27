class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        max_result = 0
        while(j>i):
            start = height[i]
            end = height[j]
            if(start>end):
                cal = end*(j-i)
                j-=1
            else:
                cal = start*(j-i)
                i+=1

            if(cal>max_result):
                 max_result = cal
        return max_result
