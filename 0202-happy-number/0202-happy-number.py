class Solution:
    def isHappy(self, n: int) -> bool:
        def squareSum(n):
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            return total

        slow = n
        fast = squareSum(n)

        while fast != 1 and slow != fast:
            slow = squareSum(slow)
            fast = squareSum(squareSum(fast))

        return fast == 1