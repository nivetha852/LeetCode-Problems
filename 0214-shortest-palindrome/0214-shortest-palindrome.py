class Solution:
    def shortestPalindrome(self, s):
        n = len(s)

        
        rev = ""
        i = n - 1

        while i >= 0:
            rev += s[i]
            i -= 1

        
        temp = s + "#" + rev
        lps = [0] * len(temp)

        j = 0
        i = 1

        while i < len(temp):

            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]

            if temp[i] == temp[j]:
                j += 1

            lps[i] = j
            i += 1

        
        longest = lps[len(temp) - 1]

        ans =""
        i = 0

        while i < n - longest:
            ans += rev[i]
            i += 1

        return ans + s