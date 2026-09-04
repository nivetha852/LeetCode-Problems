# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if not root:
            return []

        result = []
        queue = deque([root])
        leftToRight = True

        while queue:

            level = []

            for _ in range(len(queue)):
                node = queue.popleft()

                if leftToRight:
                    level.append(node.val)
                else:
                    level.insert(0, node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(level)

            leftToRight = not leftToRight

        return result