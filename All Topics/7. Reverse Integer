class Solution:
    def reverse(self, x: int) -> int:
        if x>0:
            result = int(str(x)[::-1])
        else:
            result= int(str(x * -1)[::-1]) * -1
        mini = 2 ** 31 * (-1)
        maxi = 2 ** 31 - 1
        if result > maxi or result < mini:
            return 0
        return result
