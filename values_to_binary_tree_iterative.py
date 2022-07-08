"""Convert a list of values to a binary tree using an iterative approach."""

from conftest import BinaryTreeNode


def values_to_binary_tree_iterative(values):
  parents = [BinaryTreeNode(values.pop(0))]
  root = parents[0]
  while values:
    parent = parents.pop(0)
    left_value = values.pop(0)
    if left_value:
      parent.left = BinaryTreeNode(left_value)
      parents.append(parent.left)
    if values:
      right_value = values.pop(0)
      if right_value:
        parent.right = BinaryTreeNode(right_value)
        parents.append(parent.right)
  return root