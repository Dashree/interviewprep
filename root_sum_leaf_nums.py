# 129: Sum root leaf numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        left_val = right_val = new_base = 0
        def _get_node_val(base_val, node):
            new_base = 10*base_val
            if node.left == None and node.right == None:
                return base_val
            
            left_val = right_val = 0
            if node.left != None:
                left_val = _get_node_val(new_base+node.left.val, node.left)
                
            if node.right != None:    
                right_val = _get_node_val(new_base+node.right.val, node.right)
            
            return left_val + right_val

        return _get_node_val(root.val, root)