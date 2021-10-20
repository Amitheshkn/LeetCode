class Solution:
    def reverse(self, x: int) -> int:
        high = 2 ** 31 - 1
        res = 0
        sign = 1
        if x < 0:
            sign = -1
            x = abs(x)
        while x:
            num = x % 10
            x = x//10
            if res > (high - num) // 10 :
                return 0
            res = res * 10 + num

        return res * sign