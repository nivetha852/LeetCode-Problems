class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = [0] * 101
        for h in heights:
            counts[h] += 1
            
        mismatches = 0
        expected = 1
        
        for h in heights:
            while counts[expected] == 0:
                expected += 1
            
            if h != expected:
                mismatches += 1
            
            counts[expected] -= 1
            
        return mismatches