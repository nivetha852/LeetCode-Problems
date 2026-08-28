class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left,right = 0 , len(height)-1
        leftmax,rightmax = height[left],height[right]
        res = 0
        while left < right:
            if leftmax < rightmax:
              left += 1
              leftmax = max(leftmax , height[left])
              res += leftmax - height[left]
            else:
              right -= 1 
              rightmax = max(rightmax , height[right])
              res += rightmax - height[right]
        return res