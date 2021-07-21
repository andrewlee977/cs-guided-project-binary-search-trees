"""
You are given a binary tree.

Write a function that can find the **maximum depth** of the binary tree. The
maximum depth can be defined as the number of nodes found along the longest
path from the root down to the furthest leaf node. Remember, a leaf node is a
node that has no children.

Example:

Given the following binary tree

    5
   / \
  12  32
     /  \
    8    4

your function should return the depth = 3.
"""
class BinaryTreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def maxDepth(root):
    # if the root node is None --> return 0
    if root is None:
        return 0
    # else: traverse the tree using recursion
    else:
        # call max depth passing the root's left node and store the return as left_height
        left_height = maxDepth(root.left)
        # call max depth passing the root's right node and store the return as right_height
        right_height = maxDepth(root.right)
        # max(left_height, right_height) + 1
        return max(left_height, right_height) + 1

# tests
t = BinaryTreeNode(5)
t.left = BinaryTreeNode(12)
t.right = BinaryTreeNode(32)
t.right.left = BinaryTreeNode(8)
t.right.right = BinaryTreeNode(4)

print(maxDepth(t))


# Solution 2 using STACK
def maxDepth(root):
    stack = []
    # keep track of the object and the depth of the object...
    # if the root is not none...
    if root is not None:
        # ...using a tuple (depth, node) append that to our stack
        stack.append((1, root))
    # keep track of the depth = 0
    depth = 0
    # while the stack is not empty
    while stack != []:
        # pop the current depth and root from the stack
        current_depth, root = stack.pop()
        # if the root is not None
        if root is not None:
            # update the depth w/the max of the depth and the current depth
            depth = max(depth, current_depth)
            # push the left node and the current depth + 1 onto the stack
            stack.append((current_depth + 1, root.left))
            # push the right node and the current depth + 1 onto the stack
            stack.append((current_depth + 1, root.right))
    # return the depth to the caller
    return depth


# tests
t = BinaryTreeNode(5)
t.left = BinaryTreeNode(12)
t.right = BinaryTreeNode(32)
t.right.left = BinaryTreeNode(8)
t.right.right = BinaryTreeNode(4)

print(maxDepth(t))