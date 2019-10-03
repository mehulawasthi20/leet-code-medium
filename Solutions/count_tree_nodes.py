# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        
        def trav(root,count):
            
            if root is None:
                
                return count
        
            else:
                
                count += 1
                count = trav(root.left,count)
                count = trav(root.right,count)
                
            return count
        
        
        c = trav(root,0)
        
        return c
        
       