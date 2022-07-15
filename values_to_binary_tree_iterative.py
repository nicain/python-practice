"""Convert a list of values to a binary tree using an iterative approach."""

from conftest import BinaryTreeNode


# def values_to_binary_tree_iterative(values):
#   parents = [BinaryTreeNode(values.pop(0))]
#   root = parents[0]
#   while values:
#     print(parents)
#     parent = parents.pop(0)
#     while not parent:
#       parent = parents.pop(0)
#     if values:
#       left_value = values.pop(0)
#       if left_value is not None:
#         parent.left = BinaryTreeNode(left_value)
#         parents.append(parent.left)
#       else:
#         parents.append(None)
#     if values:
#       right_value = values.pop(0)
#       if right_value is not None:
#         parent.right = BinaryTreeNode(right_value)
#         parents.append(parent.right)
#       else:
#         parents.append(None)
#     print('  ', parents)
#   return root

def values_to_binary_tree_iterative(values):

  root = BinaryTreeNode()
  all_node_list = []
  def breadth_first():
    nonlocal root, all_node_list
    next_node_list = [root]
    all_node_list.append(root)
    while next_node_list:
      curr_parent = next_node_list.pop(0)
      yield curr_parent
      curr_parent.left = BinaryTreeNode()
      curr_parent.right = BinaryTreeNode()
      next_node_list.extend([curr_parent.left, curr_parent.right])
      all_node_list.extend([curr_parent.left, curr_parent.right])
  for val, node in zip(values, breadth_first()):
    node.val = val
  for node in all_node_list:
    if node.left and node.left.val is None:
      node.left = None
    if node.right and node.right.val is None:
      node.right = None
  return root

if __name__ == "__main__":
  # root = values_to_binary_tree_iterative([0,1,2,3,4,5,6])
  # root = values_to_binary_tree_iterative([1,None,2])
  root = values_to_binary_tree_iterative([1,None,2,None, None, 3, None])
  print('===')
  print(root.val)
  print(root.left)
  print(root.right.val)
  print(root.right.left.val)
  print(root.right.right)