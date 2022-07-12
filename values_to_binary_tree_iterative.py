"""Convert a list of values to a binary tree using an iterative approach."""

from conftest import BinaryTreeNode


def values_to_binary_tree_iterative(values):
  parents = [BinaryTreeNode(values.pop(0))]
  root = parents[0]
  while values:
    parent = parents.pop(0)
    if values:
      left_value = values.pop(0)
      if left_value is not None:
        parent.left = BinaryTreeNode(left_value)
        parents.append(parent.left)
    if values:
      right_value = values.pop(0)
      if right_value is not None:
        parent.right = BinaryTreeNode(right_value)
        parents.append(parent.right)
  return root

# root = values_to_binary_tree_iterative([0,1,2,3,4,5,6])
# print(root.val)
# print(root.left.val)
# print(root.right.val)
# print(root.left.left.val)
# print(root.left.right.val)
# print(root.right.left.val)
# print(root.right.right.val)