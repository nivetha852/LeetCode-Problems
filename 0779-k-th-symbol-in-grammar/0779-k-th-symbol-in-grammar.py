class Solution(object):
    def kthGrammar(self, n, k):
        print(f"Calling kthGrammar(n={n}, k={k})")
        
        
        if n == 1:
            print(f"Base case hit: n=1, returning 0")
            return 0
        
        
        mid = 2 ** (n - 2)
        print(f"Row length mid = {mid}")
        
        if k <= mid:
            print(f"k ({k}) <= mid ({mid}): checking left half of previous row")
            result = self.kthGrammar(n - 1, k)
        else:
            print(f"k ({k}) > mid ({mid}): checking right half (flipped) of previous row")
            result = 1 - self.kthGrammar(n - 1, k - mid)
            
        print(f"Returning result {result} for kthGrammar(n={n}, k={k})")
        return result


sol = Solution()
n_val = 4
k_val = 5

print(f"--- Solving for n={n_val}, k={k_val} ---")
ans = sol.kthGrammar(n_val, k_val)
print(f"Final Answer: {ans}")