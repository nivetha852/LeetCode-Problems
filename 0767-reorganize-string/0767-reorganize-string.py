import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:

        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        maxHeap = []

        for char, freq in count.items():
            heapq.heappush(maxHeap, (-freq, char))

        prevFreq = 0
        prevChar = ""

        result = []

        while maxHeap:

            freq, char = heapq.heappop(maxHeap)

            result.append(char)

            freq += 1

            if prevFreq < 0:
                heapq.heappush(maxHeap, (prevFreq, prevChar))

            prevFreq = freq
            prevChar = char

        if len(result) == len(s):
            return "".join(result)

        return ""