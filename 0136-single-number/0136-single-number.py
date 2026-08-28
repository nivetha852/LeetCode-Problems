class Solution:
    def singleNumber(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in count:
            if count[num] == 1:
                return num

        return -1