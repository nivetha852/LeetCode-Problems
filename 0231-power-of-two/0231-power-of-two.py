class Solution:
    def isPowerOfTwo(self, n: int):
        return n > 0 and (n ^ (n-1)) == (2*n-1)