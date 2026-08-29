class Solution(object):
    def restoreIpAddresses(self, s):

        result = []

        def backtrack(index, current):

            if len(current) == 4:
                if index == len(s):
                    result.append(".".join(current))
                return

            for length in range(1, 4):

                if index + length > len(s):
                    break

                part = s[index:index + length]

            
                if len(part) > 1 and part[0] == '0':
                    continue

                
                if int(part) > 255:
                    continue

                current.append(part)

                
                backtrack(index + length, current)

                
                current.pop()

        backtrack(0, [])

        return result