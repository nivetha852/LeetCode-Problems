class Solution(object):
    def wiggleSort(self, nums):
        res = sorted(nums)

        n = len(nums)
        left = (n - 1) // 2
        right = n - 1

        for i in range(n):
            if i % 2 == 0:
                nums[i] = res[left]
                left -= 1
            else:
                nums[i] = res[right]
                right -= 1