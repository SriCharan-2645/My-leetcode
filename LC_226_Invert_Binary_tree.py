"""
226. Invert Binary Tree
Easy
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursion break statement
        if not root:
            return None
        # swap children
        temp = root.left
        root.left = root.right
        root.right = temp
        # recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


"""
The time complexity of the `invertTree` function is O(n), where "n" is the number of nodes in the binary tree.

Here's why:

1. **Traversal:** The function traverses the entire binary tree, visiting each node exactly once. This is a linear 
operation with a time complexity of O(n), where "n" is the number of nodes.

2. **Swapping:** For each node, the function performs a constant-time operation by swapping the left and right child 
nodes. This swap operation is not dependent on the size of the tree and does not contribute to the overall time 
complexity.

3. **Recursive Calls:** The function makes two recursive calls, one on the left subtree and one on the right subtree. 
However, since each node is visited only once, the total number of recursive calls made is proportional to the number 
of nodes, which is O(n).

The dominant factor in the time complexity is the traversal of the tree, which has a time complexity of O(n). 
Therefore, the overall time complexity of the `invertTree` function is O(n).
"""
