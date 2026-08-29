class Solution:
    def letterCombinations(self, digits):
        if digits == "":
            return []

        phone = {
            "2": "abc", "3": "def",
            "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }

        result = [""]

        for d in digits:
            temp = []
            for x in result:
                for y in phone[d]:
                    temp.append(x + y)
            result = temp

        return result