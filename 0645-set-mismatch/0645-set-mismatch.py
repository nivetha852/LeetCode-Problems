class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        seen = set()
        duplicate = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        total = n * (n + 1) // 2
        missing = total - (sum(nums) - duplicate)

        return [duplicate, missing]