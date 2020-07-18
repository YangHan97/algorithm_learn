import functools
class Solution:
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n
        a, b, temp = 1, 2, 0
        for i in range(3, n+1):
            temp = a + b
            a = b
            b = temp