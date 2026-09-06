class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def solve(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            if (i, total) in dp:
                return dp[(i, total)]

            plus = solve(i + 1, total + nums[i])
            minus = solve(i + 1, total - nums[i])

            dp[(i, total)] = plus + minus

            return dp[(i, total)]

        return solve(0, 0)