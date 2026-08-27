class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        
        count = {}

        for num in arr1:
            count[num] = count.get(num, 0) + 1

        result = []

        for num in arr2:
            if num in count:
                result += [num] * count[num]
                del count[num]

        remaining = []

        for num in count:
            remaining += [num] * count[num]

        remaining.sort()

        return result + remaining