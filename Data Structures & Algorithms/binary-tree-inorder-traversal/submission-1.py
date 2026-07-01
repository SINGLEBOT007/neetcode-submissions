# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # INODER ITERATIVE
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
        # # INODER RECURSION
        # res = []
        # def inoder(root):
        #     if not root:
        #         return None
            
        #     inoder(root.left)
        #     res.append(root.val)
        #     inoder(root.right)
        
        # inoder(root)
        # return res

        