class Solution(object):
    def maxProduct(self, nums):

        maximum = nums[0]
        minimum = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:
                maximum, minimum = minimum, maximum

            maximum = max(num, maximum * num)
            minimum = min(num, minimum * num)

            answer = max(answer, maximum) 
        return answer