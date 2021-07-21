class BTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add(self, value):
        new_node = BTNode(value)
        if value < self.value:
            # go left
            if self.left is not None:
                self.left.add(value)
            else:
                self.left = new_node
        else:
            # go right
            if self.right is not None:
                self.right.add(value)
            else:
                self.right = new_node

    def search(self, target):
      if self.value == target:
        return self
      elif target < self.value:
        if self.left is None:
          return False
        else:
          return self.left.search(target)
      else:
        if self.right is None:
          return False
        else:
          return self.right.search(target)


t = BTNode(10)
t.add(20)
t.add(5)
t.add(7)
print(t.right.value)
print(t.left.right.value)
t5 = t.search(7)
print(t5.value)



"""
BinarySearchTree - Tree data structure. With some rules...

1. If we add an item to the tree. If the value of that item
is less than the value of its parent then place it to the left
of the parent. Otherwise place it to the right of the parent

        10
      /    \
     5      20
      \    /
       7  15
"""