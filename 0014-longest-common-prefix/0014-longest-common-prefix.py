class Solution:
    def longestCommonPrefix(self, strs):

        if not strs:
            return""
        reference = strs[0]
        for char_index in range(len(reference)):
            current_char = reference[char_index]
            for word in strs[1:]:
                if char_index == len(word)or word[char_index]!=current_char:
                    return reference[:char_index]
        return reference