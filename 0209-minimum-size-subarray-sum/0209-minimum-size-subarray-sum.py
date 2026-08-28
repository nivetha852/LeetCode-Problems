class Solution:

    def minSubArrayLen(self, target, nums):

        left, current_sum = 0, 0

        min_len = float('inf')

        for right in range(len(nums)):

            current_sum += nums[right]

            while current_sum >= target:

                min_len = min(min_len, right - left + 1)

                current_sum -= nums[left]

                left += 1

        if min_len == float('inf'):

            return 0

        return min_len